#!/usr/bin/env python
# coding: utf-8

import os
import numpy as np
import pandas as pd
from pprint import pprint

def open_dataset(file_name):
    return pd.read_csv(filepath_or_buffer=file_name, delimiter="\t", encoding="utf-8", header=0)

itineraries = open_dataset('data_sncf/timetables.csv')
# itineraries = open_dataset('data_sncf/test.csv')
itineraries = itineraries.sort_values(by=['trip_id', 'trajet', 'duree'], ascending=[True, True, True])

# dataframe refacto 
trajet_splited = itineraries['trajet'].str.split(' - ')

itineraries['start'] = trajet_splited.str[0]
itineraries['end'] = trajet_splited.str[1]

itineraries.drop('trajet', axis=1, inplace=True)


# Filter all possible localisations
locsStart = itineraries['start'].tolist()
locsEnd = itineraries['end'].tolist()
locs = list(dict.fromkeys(locsStart + locsEnd))


# get all possible itineraries from un localisation
def get_itineraries(fromLoc):
    return itineraries.loc[itineraries['start'] == fromLoc]


# update distance of localisation from source
def updateDistanceFromSource(matrix, itineraries):
    # print(itineraries)
    
    for index, row in itineraries.iterrows():
        
        # if initerary is not yet processed
        if matrix[row['end']]['processed'] == False:
        
            oldValue = matrix[row['end']]['distanceFromSource']
            newValue = matrix[row['start']]['distanceFromSource'] + row['duree']
            
            if oldValue == 'infinite':
                matrix[row['end']]['distanceFromSource'] = newValue
                matrix[row['end']]['fromLoc'] = row['start']
            else:   
                if newValue < oldValue:
                    matrix[row['end']]['distanceFromSource'] = newValue
                    matrix[row['end']]['fromLoc'] = row['start']
        
        
    # print("-----------------------------------------------------------------")
    # print("---------- MISE A JOUR DES DISTANCES DEPUIS LA SOURCE -----------")
    # print("-----------------------------------------------------------------")
    # print(" ")
    
    return matrix


# Find the minimum distance that has not been processed and that is not infinite
def findMiniDistanceFromSource(matrix):
    
    toProcess = {}
    
    for index, row in matrix.items():
        if row['processed'] == False and row['distanceFromSource'] != 'infinite':
            toProcess[index] = row
            
    # print("-------------------- Les itineraires pas encore traités ---------------------")
    # print(" ")
    # [print(key,':',value) for key, value in toProcess.items()]
    # print(" ")
    
    miniValue = 9999999999
    location = ""
    
    for index, row in toProcess.items():
    
        if row['distanceFromSource'] < miniValue:
            miniValue = row['distanceFromSource']
            location = index
            
       
    # if location != "":    
    #     print("-------------------- La distance la plus courte pas encore traitée ---------------------")
    #     print(" ")
    #     print("Etape : ", location, " - Distance depuis la source : ", miniValue)
    #     print(" ")
    # else:
    #     print("------------------------------------------------------------------------")
    #     print("-------------------- Plus de trajets lié à traiter ---------------------")
    #     print("------------------------------------------------------------------------")
    #     print(" ")
        
    return location
    

# find the shortest distance between source and destination 
def get_best_itinerary(matrix, source, destination):
    toProcess = {}
    distance = ""
    fromLoc = ""
    itineraries = []
    
    for index, row in matrix.items():
        if row['processed'] == True and row['distanceFromSource'] != 'infinite':
            toProcess[index] = row
            
    # print(toProcess)
    if destination in toProcess.keys():
        # print(toProcess[destination])
        distance = toProcess[destination]["distanceFromSource"]
        fromLoc = toProcess[destination]["fromLoc"]
        itineraries.insert(0, destination)
        
        while fromLoc != source:
            itineraries.insert(0, fromLoc)
            fromLoc = toProcess[fromLoc]["fromLoc"]
            
        itineraries.insert(0, source)
        
        return {
            'itineraries': itineraries,
            'distance': distance
        }
    
    else:
        print("-----------------------------------------------------------------")
        print("-------------------- Ce trajet n'existe pas ---------------------")
        print("-----------------------------------------------------------------")
        print("")
        
        return "None"


# Find the shortest path among all possible sources and destinations 
def dijsktra(df, source, destination):
    matrixLoc = {}
    
    locsStart = df['start'].tolist()
    locsEnd = df['end'].tolist()
    locs = list(dict.fromkeys(locsStart + locsEnd))
    
    # filter possible localisations
    locsStart = list(filter(lambda k: source in k, locs))
    locsEnd = list(filter(lambda k: destination in k, locs))
    
    # print(locsStart)
    # print(locsEnd)
    
    returnResult = "None"

    for locStart in locsStart:
        matrixLoc = {}
        
        for locEnd in locsEnd:
            if locEnd == locStart:
                continue
            
            matrixLoc = {}
    
            # print("Trajet : ", locStart, " - ", locEnd)
            # print(" ")
            
            # initialize matrix
            for loc in locs:
                matrixLoc[loc] = {
                    'distanceFromSource': 'infinite',
                    'fromLoc': '',
                    'processed': False,
                }
                
            # initialize matrix source values
            matrixLoc[locStart]['distanceFromSource'] = 0
            matrixLoc[locStart]['fromLoc'] = locStart
            matrixLoc[locStart]['processed'] = True
            
            nextLocation = locStart
            
            while nextLocation != "":

                if not get_itineraries(nextLocation).empty:
                    matrixLoc = updateDistanceFromSource(matrixLoc, get_itineraries(nextLocation))
                # else:
                    # print("Aucun itinéraire en partant de ", nextLocation)
                    # print(" ")
                    
                nextLocation = findMiniDistanceFromSource(matrixLoc)

                if nextLocation != "":
                    matrixLoc[nextLocation]['processed'] = True
            
            result = get_best_itinerary(matrixLoc, locStart, locEnd)
            
            if result != "None":
                return result

    return "None"
    

def get_step_itinerary(df, source, destination):
    result = dijsktra(df, source, destination)
    resultReversed = dijsktra(df, destination, source)
    resultToReturn = False
    
    if resultReversed != "None":
        itineraries = resultReversed['itineraries']
        itineraries.reverse()
        resultReversed['itineraries'] = itineraries
            
    if result == "None" and resultReversed != "None":
        resultToReturn = resultReversed
    
    if resultReversed == "None" and result != "None":
        resultToReturn = result
    
    if resultReversed != "None" and result != "None":
            
        if resultReversed['distance'] < result['distance']:
            resultToReturn = resultReversed
        else:
            resultToReturn = result
    
    return resultToReturn
    

def get_itinerary(df = itineraries, locArray = []):
    print(f"I am in {locArray}")
    
    fullTrip = []
    distance = 0
    
    while len(locArray) >= 2:
        # print(locArray)
        locStart = locArray[0]
        locEnd = locArray[1]
        
        # print(locStart)
        # print(locEnd)
        
        result = get_step_itinerary(df, locStart, locEnd)
        
        if result != "None":
            fullTrip = fullTrip + result['itineraries']
            distance = distance + result['distance']
            locArray.pop(0)
            
        else:
            print("-----------------------------------------------------------------")
            print("---------------------- Aucun trajet trouvé ----------------------")
            print("-----------------------------------------------------------------")
            print("")
            
            return
        
    
    fullTrip = list(dict.fromkeys(fullTrip))
    
    return {
            'distance': distance,
            'itineraries': fullTrip
    }
