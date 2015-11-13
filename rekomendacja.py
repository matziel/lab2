#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  Wzorowane na przykladzie Rona Zacharskiego

from math import sqrt

users = {"Ania": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0},
         "Bonia":{"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},
         "Celina": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5, "Slightly Stoopid": 1.0},
         "Dominika": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 2.0},
         "Ela": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0, "Vampire Weekend": 1.0},
         "Fruzia":  {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 4.0},
         "Gosia": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0, "Slightly Stoopid": 4.0, "The Strokes": 5.0},
         "Hela": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5, "The Strokes": 3.0}
        }



def manhattan(rating1, rating2):
    """Oblicz odleglosc w metryce taksowkowej miedzy dwoma zbiorami ocen
       danymi w postaci: {'The Strokes': 3.0, 'Slightly Stoopid': 2.5}
       Zwraca -1, gdy zbiory nie maja wspolnych elementow"""
    klucze1 = rating1.keys()
    klucze2 = rating2.keys()
    odleglosc = 0
    udaloSiePorownac = False
    
    for klucz in klucze1 :
        if klucz in rating2.keys():
            udaloSiePorownac = True
            odleglosc = odleglosc + abs(rating2[klucz] - rating1[klucz]) 

    if udaloSiePorownac:
        return odleglosc
    else:
        return -1

def testManhattan(rating1, rating2, odleglosc):
    if manhattan(rating1, rating2) == odleglosc:
        return True
    else:
        return False

def computeNearestNeighbor(imie, uzytkownicy):
    """dla danego uzytkownika, zwraca liste innych uzytkownikow wedlug bliskosci preferencji"""
    odleglosci = []
    for imie2 in uzytkownicy:
        odleglosc = 0
        if imie!=imie2:
            odleglosc = manhattan(uzytkownicy[imie], uzytkownicy[imie2])
            odleglosci.append((odleglosc, imie2))
    return sorted(odleglosci)

#print(computeNearestNeighbor('Hela',users))

def recommend(username, users):
    """Zwraca liste rekomendacji dla uzytkownika"""
    # znajduje preferencje najblizszego sasiada
    nearestName = computeNearestNeighbor(username, users)[0][1]
    print username
    print 'Najblizszy sasiad to: %s' %nearestName
    recommendations = []
    ratingOfNearest = users[nearestName]
    print ('Rekomendacje to: ')
    print (ratingOfNearest)
    # Rekomenduje wykonawce, ktorego uzytkownik nie ocenil, a zrobil to jego najblizszy sasiad
    userRating = users[username]
    
    for artist in ratingOfNearest:
        if not artist in userRating:
            recommendations.append((artist, ratingOfNearest[artist]))
        return sorted(recommendations, key=lambda artistTuple: artistTuple[1], reverse = True)

#recommend('Hela', users)
print(recommend('Hela', users))
