# --- Fixed variables ---
AVG_HUMAN_NWALKING_SPEED = 1 # Normal Walking : in meters/s
AVG_HUMAN_FWALKING_SPEED = 1.4 # Fast Walking : in meters/s
AVG_HUMAN_RUNNING_SPEED = 1.8 # Running : in meters/s

# --- Tests persons ---
PERSON1 = (12.6,3.2)
PERSON2 = (35,32.7)
PERSON3 = (83.9,37)

# --- Main classes ---
class Stop:
    def __init__(self, name, position, waiting_time, stop_time, delay = None):
        self.id = name
        self.position = position
        self.waiting_time = waiting_time
        self.stop_time = stop_time
        self.delay = delay


# --- Train hours ---

# X:minutes (the times shown are in units of minutes)
horaires_u = 15 # Urbaine : ~/15 mins
horaires_i = 15 # Industrielle : ~/15 mins
horaires_m = 20 # Maritime : ~/20 mins
horaires_b = 15 # Banlieu : ~/15 mins
horaires_c = 10 # Ville Centre : ~/10 mins


# --- All train stops ---

# Zone Urbaine :
UH = Stop("UH", (17.6,5.5), 5, 5)
U1 = Stop("U1", (6.2,7), horaires_u, 1)
U2 = Stop("U2", (12.3,1.2), horaires_u, 1)
U3 = Stop("U3", (28.5,3.3), horaires_u, 1)
U4 = Stop("U4", (2.9,16.3), horaires_u, 1)
U5 = Stop("U5", (14,12), horaires_u, 1)
U6 = Stop("U6", (32.6,10.7), horaires_u, 1)
U7 = Stop("U7", (38.2,3.5), horaires_u, 1)
U8 = Stop("U8", (45.3,7.6), horaires_u, 1)
U9 = Stop("U9", (55.6,3.7), horaires_u, 1)

# Zone Industrielle :
IH = Stop("IH", (8.2,67.6), 5, 5)
I1 = Stop("I1", (4.3,59.7), horaires_i, 1)
I2 = Stop("I2", (11.7,61.8), horaires_i, 1)
I3 = Stop("I3", (10,53.6), horaires_i, 1)
I4 = Stop("I4", (7.6,45.7), horaires_i, 1)
I5 = Stop("I5", (3.7,38.8), horaires_i, 1)

# Zone Maritime :
M1 = Stop("M1", (55.3,69.4), horaires_m, 1)
M2 = Stop("M2", (65,65), horaires_m, 1)
M3 = Stop("M3", (76.2,62.1), horaires_m, 1)
M4 = Stop("M4", (84.4,57), horaires_m, 1)
M5 = Stop("M5", (90,49.5), horaires_m, 1)
M6 = Stop("M6", (94.6,43), horaires_m, 1)

# Banlieu :
BH = Stop("BH", (77.3,17), 5, 5)
B1 = Stop("B1", (75.5,23.3), horaires_b, 1)
B2 = Stop("B2", (80.7,22), horaires_b, 1)
B3 = Stop("B3", (83.7,16.8), horaires_b, 1)
B4 = Stop("B4", (74.4,11.2), horaires_b, 1)

# Ville Centre :
CH = Stop("CH", (48.2,38.5), 5, 5)
C1 = Stop("C1", (50.4,17.8), horaires_c, 1)
C2 = Stop("C2", (64.8,26.1), horaires_c, 1)
C3 = Stop("C3", (68.8,40.2), horaires_c, 1)
C4 = Stop("C4", (61.8,54), horaires_c, 1)
C5 = Stop("C5", (45.8,59), horaires_c, 1)
C6 = Stop("C6", (31.5,50.8), horaires_c, 1)
C7 = Stop("C7", (27.7,36.8), horaires_c, 1)
C8 = Stop("C8", (34.5,22.8), horaires_c, 1)
C9 = Stop("C9", (49.3,27.3), horaires_c, 1)
C10 = Stop("C10", (56.6,31.8), horaires_c, 1)
C11 = Stop("C11", (58.6,39), horaires_c, 1)
C12 = Stop("C12", (55,46.5), horaires_c, 1)
C13 = Stop("C13", (46.9,49), horaires_c, 1)
C14 = Stop("C14", (39.5,46.5), horaires_c, 1)
C15 = Stop("C15", (37.5,37.5), horaires_c, 1)
C16 = Stop("C16", (41.3,30.3), horaires_c, 1)
# --  
C20 = Stop("C20", (17,24), horaires_c, 1)
C21 = Stop("C21", (18.3,41.5), horaires_c, 1)
C22 = Stop("C22", (34.9,65.1), horaires_c, 1)
C23 = Stop("C23", (82,31.8), horaires_c, 1)
C24 = Stop("C24", (54.1,11), horaires_c, 1)

# --- All train stops ---
stops = [UH, U1, U2, U3, U4, U5, U6, U7, U8, U9, IH, I1, I2, I3, I4, I5, M1, M2, M3, M4, M5, M6, BH, B1, B2, B3, B4, CH, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, C13, C14, C15, C16, C20, C21, C22, C23, C24]

# --- All train links & times ---
connections = {"UH": [(U1,5), (U2,3), (U3,5), (U5,4), (C8,8)], "U1": [(UH,5)], "U2": [(UH,3)], "U3": [(UH,5)], "U4": [(I5,3), (U5,5)], "U5": [(UH,4), (U4,5), (U6,6)], "U6": [(U5,6), (U8,5)], "U7": [(U8,4)], "U8": [(U6,5), (U7,4), (U9,5)], "U9": [(U8,5), (BH,3)],
            "IH": [(I1,5), (I2,3), (C6,3)], "I1": [(IH,5)], "I2": [(IH,3), (I3,5)], "I3": [(I2,5), (I4,5)], "I4": [(I5,5), (I3,5)], "I5": [(I4,5), (U4,3)],
            "M1": [(C4,7), (M2,5)], "M2": [(M1,5), (M3,5)], "M3": [(M2,5), (C4,6), (M4,5)], "M4": [(M3,5), (M5,5)], "M5": [(C4,8), (M4,5), (M6,6)], "M6": [(M5,6)],
            "BH": [(B1,3), (B2,2), (B3,2), (B4,2), (C2,2.5), (U9,3)], "B1": [(BH,3)], "B2": [(BH,2)], "B3": [(BH,2)], "B4": [(BH,2)],
            "CH": [(C16,1), (C10,1), (C14,1), (C12,1)], "C1": [(C24,3), (C8,5), (C9,3), (C2,5)], "C2": [(BH,2.5), (C10,1), (C1,5), (C3,5)], "C3": [(C2,5), (C23,4), (C4,5), (C11,3)], "C4": [(C3,5), (M5,8), (M3,6), (M1,7), (C5,5), (C12,1)], "C5": [(C22,5), (C4,5), (C13,3), (C6,5)], "C6": [(C5,5), (C14,1), (IH,3), (C7,5)], "C7": [(C6,5), (C15,3), (C8,5), (C20,5), (C21,3)], "C8": [(C7,5), (UH,3), (C1,5), (C16,1)],
            "C9": [(C1,3), (C10,3), (C16,3)], "C10": [(C2,1), (C11,3), (CH,1), (C9,3)], "C11": [(C10,3), (C3,3), (C12,3)], "C12": [(CH,1), (C11,3), (C4,1), (C13,3)], "C13": [(C5,3), (C14,3), (C12,3)], "C14": [(C6,1), (C15,3), (CH,1), (C13,3)], "C15": [(C7,3), (C14,3), (C16,3)], "C16": [(C15,3), (CH,1), (C9,3), (C8,1)],
            "C20": [(C7,5)], "C21": [(C7,3)], "C22": [(C5,5)], "C23": [(C3,4)], "C24": [(C1,3)] }
# {"name_of_the_stop" : ("linked_stop", time_of_travel), ... }



# --- Time functions ---

def minutes(hours, minutes):
    ''' :desc: Converts hours:minutes into minutes
        :param: Entries: hours (int) // minutes (int)
        :param: Outs : time in minutes '''
    return hours*60 + minutes

def hours(minutes):
    ''' :desc: Converts minutes to hours,minutes
        :param: Entries: minutes (int)
        :param: Outs: hours,minutes (%60) '''
    return (minutes//60, minutes%60)

def distance(my_position, to_position):
    ''' :desc: Calculates a distance from coordinates (x,y)
        :param: Entries: my_position (tuple x,y) // to_position (tuple x,y)
        :param: Outs: The distance between the two positions '''
    import math
    vector_x = to_position[0] - my_position[0]
    vector_y = to_position[1] - my_position[1]
    return round(math.sqrt(vector_x**2 + vector_y**2)*100, 2) #En metres

def time_on_foot(distance, walking_type):
    ''' :desc: Indicates the time required to traverse a distance at a given walking speed
        :param: Entries: 'distance' to traverse (int in meters) // 'walking_type' (VARIABLE)
        :param: Outs: time (in minutes) of walking required to traverse the 'distance' '''
    return round((distance/(walking_type/1.5))/60, 2)

def time_to_arrival(train, actual_time):
    ''' :desc: Time until the arrival of the train depending on its timetable
        :param: Entries: 'train' (stop) // 'actual_time' (in minutes)
        :param: Outs: time (float in minutes) until the arrival of the train '''
    return 0 if actual_time%train.waiting_time == 0 else train.waiting_time - actual_time%train.waiting_time

def travel_time(from_stop, to_stop):
    ''' :desc: Travel time by train
        :param: Entries: 'from_stop' (stop) // 'to_stop' (stop)
        :param: Outs: travel time (float in minutes) '''
    for i in connections[from_stop]:
        if i[0].id == to_stop:
            return i[1]
    return False # Route inéxistante



# --- Paths / routes functions ---

def diff_list(liste1, liste2):
    ''' :desc: Only keep the differences between list1 and list2
        :param: Entries: 'list1' (list) // 'list2' (list)
        :param: Outs: a list with only elements that are present in 'liste1' but not in 'liste2' '''
    list_temp = liste1[:]
    for i in liste1:
        if i in liste2:
            list_temp.remove(i)
    return list_temp

def possible_directions(from_stop, to_stop):
    ''' :main: All possible directions from one stop
        :param: Entries: 'from_stop' (stop) // 'to_stop' (stop)
        :param: Outs: a list of all possible directions from one stop '''
    if from_stop.id[0] == to_stop.id[0]: # Si je suis dans le block où je veux aller, j'élimine les directions qui me font en sortir
        return [i[0] for i in connections[from_stop.id] if i[0].id[0] == to_stop.id[0]]
    pos = [i[0] for i in connections[from_stop.id] if i[0].id[0] == to_stop.id[0]]
    return pos if len(pos) > 0 else [i[0] for i in connections[from_stop.id]] # Si je peux aller dans le bloc de destination_coordinates, alors je ne prend en compte que les chemins qui m'y mènenent et pas les autres

def stop_to_id(list):
    ''' :desc: Converts a list of stops to a list of stop ids
        :param: Entries: 'list' (list) to convert
        :param: OUts: converted list (list) '''
    return [i.id for i in list]

def path_time(parcours, minutes, base):
    ''' :desc: Indicates how much time is needed for an entire route (counting waiting at each stops, walking...)
        :param: Entries: route (list of stops) // minutes (actual times in int 'minutes')
        :param: Outs: total time needed for the route '''
    if len(parcours) <= 1: return minutes - base
    return path_time(parcours[1:], minutes + time_to_arrival(parcours[0], minutes) + travel_time(parcours[0].id, parcours[1].id), base)

def two_nearest_stops(initial_coordinates):
    ''' :desc: Gives the two nearest stops from a position
        :param: Entries: 'initial_coordinates' (tuple x,y) from where we start
        :param: Outs: a list (list) of 2 nearest (sorted) stops '''
    return sorted([(distance(initial_coordinates, i.position), i) for i in stops])[0:2]

def nearest_stop(initial_coordinates):
    ''' :desc: Gives the nearest stop from a position
        :param: Entries: 'initial_coordinates' (tuple x,y) from where we start
        :param: Outs: nearest stop (stop) '''
    return sorted([(distance(initial_coordinates, i.position), i) for i in stops])[0]




# --- All possible paths Algorithm ---

def possible_paths(starting_stop, destination_coordinates_stop, taken_stops = [], rang = 0, end = []):
    ''' :MAIN: Recursive function - Returns a list of all possible routes from one stop to another
        :param: Entries: 'starting_stop' (stop) // 'destination_coordinates_stop' (stop)
        :param: Outs: a list of all possible routes from 'starting_stop' to 'destination_coordinates_stop' '''
    possible_ways = stop_to_id(diff_list(possible_directions(starting_stop, destination_coordinates_stop), taken_stops))
    # Afficher la recursion: print(possible_ways, starting_stop.id, stop_to_id(taken_stops), len(set([i.id[0] for i in taken_stops])))

    # Si on change de bloc plus de 3x sans arriver dans le bloc où est notre destination_coordinates_stop, on coupe la branche.
    if len(set([i.id[0] for i in taken_stops])) > 3 and starting_stop.id[0] != destination_coordinates_stop.id[0]: return False

    # Si nous sommes arrivés, ou que notre destination_coordinates est à la prochaine gare, considérer que nous sommes arrivé, et renvoyer le chemin utilisé.
    if rang > 0:
        if starting_stop.id == destination_coordinates_stop.id: return taken_stops + [destination_coordinates_stop]
        elif destination_coordinates_stop.id in possible_ways: return taken_stops + [starting_stop] + [destination_coordinates_stop]

    # Si il y a plus de chemin possible et que nous ne sommes pas à destination_coordinates, couper la branche.
    if len(possible_ways) == 0: return False

    # Pour chaque destination_coordinates possible, repeter à partir de la destination_coordinates suivante, jusqu'à arriver à destination_coordinates.
    for i in diff_list(possible_directions(starting_stop, destination_coordinates_stop), taken_stops): 
        # On creer une variable qui prend la valeure de la branche pour pouvoir l'analyser et la garder seulement si intéressante.
        app = possible_paths(i, destination_coordinates_stop, taken_stops + [starting_stop], rang+1, end)
        if app not in [False, None] and len(app) < 10 and type(app) == list: end.append(app)
    
    # Si on est revenu à la racine de l'arbre, on a tout essayé, et on return donc les possibilités parcourues.
    if rang == 0: return end



# --- Launching algorithm ---

def best_path(initial_coordinates, destination_coordinates, hours, mins, walking_speed): # 'hours' et 'mins' correspondent à l'heure où vous partez. Exemple : 3,40 (3 heures 40)
    ''' :MAIN: Find the best course and its best alternative for you to choose from
        :param: Entries: 'initial_coordinates' (tuple x,y) // 'destination_coordinates_coordinates' (tuple x,y) // 'hours' actual hour (int) // 'minutes' actual minutes (int) // 'walking_speed' (VARIABLE)
        :param: Outs : Prints out all the information about the routes and times // and returns the route or 'By walk.'. '''

    to_minutes = minutes(hours, mins)
    arret_de_destination = nearest_stop(destination_coordinates) # (distance, stop)
    arret_plus_proche1, arret_plus_proche2 = two_nearest_stops(initial_coordinates)[0], two_nearest_stops(initial_coordinates)[1] # (distance, stop)

    chemins_possibles = [paths for paths in possible_paths(arret_plus_proche1[1], arret_de_destination[1])] + [paths for paths in possible_paths(arret_plus_proche2[1], arret_de_destination[1])]
    #return chemins_possibles

    meilleur_chemin = sorted([(path_time(chaque_chemin, to_minutes, to_minutes) + time_on_foot(distance(initial_coordinates, chaque_chemin[0].position), walking_speed) + time_on_foot(distance(destination_coordinates, chaque_chemin[-1].position), walking_speed), [chemin.id for chemin in chaque_chemin]) for chaque_chemin in chemins_possibles], key = lambda x: (x[0], len(x[1])))[0]
    #return meilleur_chemin

    best_route = " > ".join(meilleur_chemin[1])
    by_walk_only_time = time_on_foot(distance(initial_coordinates, destination_coordinates), walking_speed)

    if by_walk_only_time+2 < meilleur_chemin[0]: # On privilege la marche à 2 minutes près
        print(f"The best route is to go on foot ! Estimated time : {round(by_walk_only_time)} minutes.")
        ending_choice = "By walk."
    else: # Si plus rapide pas à pied
        print(f"The best route we have found is : Depart (en marchant) > {best_route} > Arrivée (en marchant). It will take you {round(meilleur_chemin[0])} minute(s).")
        print(f"On walk, it would take you : {round(by_walk_only_time)} minutes.")
        ending_choice = f"Depart (en marchant) > {best_route} > Arrivée (en marchant)."

    return ending_choice




# --- Using tests ---

print("\nFrom PERSON1 >to> U2 :")
best_path(PERSON1, U2.position, 0, 0, AVG_HUMAN_NWALKING_SPEED)

print("\nFrom PERSON1 >to> UH :")
best_path(PERSON1, UH.position, 5, 0, AVG_HUMAN_NWALKING_SPEED)

print("\nFrom M6 >to> M4 :")
best_path(M6.position, M4.position, 5, 0, AVG_HUMAN_NWALKING_SPEED)

print("\nFrom PERSON1 >to> PERSON2 :")
best_path(PERSON1, PERSON2, 5, 0, AVG_HUMAN_NWALKING_SPEED)

print("\nFrom PERSON1 >to> UH :")
best_path(PERSON1, UH.position, 5, 0, AVG_HUMAN_NWALKING_SPEED)

print("\nFrom PERSON2 >to> C23 :")
best_path(PERSON2, C23.position, 5, 0, AVG_HUMAN_NWALKING_SPEED)

print("\nFrom PERSON2 >to> PERSON3 :")
best_path(PERSON2, PERSON3, 5, 0, AVG_HUMAN_NWALKING_SPEED)

print("\nFrom PERSON3 >to> PERSON1 :")
best_path(PERSON3, PERSON1, 5, 0, AVG_HUMAN_NWALKING_SPEED)


# --- Tests for all possibilites ---
'''
for i in range(0,len(stops)):
    for e in range(0,len(stops)):
        print(best_path(stops[i].position, stops[e].position, 0, 0, AVG_HUMAN_NWALKING_SPEED))
'''