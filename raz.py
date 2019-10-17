#!/usr/bin/python3

import random
import json
from time import gmtime, strftime

guesses_list = [(8,4,33,9,14,5),(23,3,6,17,28,15),(21,19,9,6,3,8),(4,14,16,31,36,37),(11,15,17,32,34,35),(5,20,21,25,26,32),(6,12,13,14,18,32),(7,12,16,22,24,33),(4,14,21,25,29,30),(1,4,12,19,22,26),(4,5,13,22,27,34),(1,8,16,21,28,34),(2,6,18,24,29,31),(7,9,13,17,26,36),(5,15,16,18,23,30),(10,11,18,23,26,28),(1,2,27,30,32,36),(2,25,26,31,33,34),(2,3,20,22,35,36),(7,12,27,28,31,35),(10,13,15,19,20,31),(2,5,11,12,29,37),(8,17,20,27,29,33),(6,7,10,16,25,35),(2,4,8,9,18,24),(10,14,17,22,24,37),(3,7,15,18,27,37),(1,7,11,13,23,24),(1,9,30,33,35,37),(3,19,24,28,30,34),(1,6,11,30,12,10),(17,31,19,18,25,28),(27,26,29,16,32,24),(10,9,5,37,6,20),(22,21,25,28,32,31),(27,21,18,22,6,14),(22,9,8,35,28,4),(22,20,11,14,3,1),(27,29,10,7,31,5),(35,21,23,14,15,12),(4,3,15,33,6,11),(32,7,3,19,2,5),(24,15,5,26,6,3),(2,23,28,17,5,1),(37,21,20,25,13,26),(30,26,22,15,31,14),(9,29,35,26,32,33),(28,33,32,19,14,5),(1,25,15,29,31,3),(10,15,23,18,19,36),(24,25,21,18,19,35),(6,7,9,12,14,34),(4,7,5,6,8,36),(6,30,20,2,17,16),(1,5,35,13,15,33),(23,25,27,32,35,4),(31,11,8,6,23,15),(3,12,13,7,30,20),(12,17,13,21,23,29),(8,25,13,30,18,34),(1,18,4,20,31,32),(23,37,22,31,19,29),(23,34,18,33,3,10),(25,33,36,14,21,11),(2,14,7,10,13,21),(32,37,4,17,8,10),(24,25,29,36,12,30),(34,36,28,29,26,27),(20,23,24,28,30,34),(37,34,30,31,16,19),(9,29,35,26,32,33),(9,3,19,11,16,27),(2,15,8,12,26,1),(13,16,28,9,25,33)]

# x37=fast_combination_set6(37)
# x8=fast_combination_set6(8)
def fast_combination_set6(options):
    print(strftime("%Y-%m-%d %H:%M:%S", gmtime()) + ' - generating 6 balls in ' +str(options)+ ' options...')
    result=set()
    for i in range(options):
        for j in range(options):
            if j==i: break
            for k in range(options):
                if k==i or k==j: break
                for x in range(options):
                    if x==i or x==j or x==k: break
                    for y in range(options):
                        if y==i or y==j or y==k or y==x: break
                        for z in range(options):
                            if z==i or z==j or z==k or z==x or z==y: break
                            unique_numbers = set()
                            unique_numbers.add(i+1)
                            unique_numbers.add(j+1)
                            unique_numbers.add(k+1)
                            unique_numbers.add(x+1)
                            unique_numbers.add(y+1)
                            unique_numbers.add(z+1)
                            if len(unique_numbers) == 6:
                                result.add(tuple(sorted((i+1, j+1, k+1, x+1, y+1, z+1))))
    print(strftime("%Y-%m-%d %H:%M:%S", gmtime()) + ' - done, ' +str(len(result))+ ' combinations.' )
    return len(result), result

# generates all triples
def fast_combination_set3(options):
    print(strftime("%Y-%m-%d %H:%M:%S", gmtime()) + ' - generating 3 balls in ' +str(options)+ ' options...')
    result=set()
    for i in range(options):
        for j in range(options):
            if j==i: break
            for k in range(options):
                if k==i or k==j: break
                unique_numbers = set()
                unique_numbers.add(i+1)
                unique_numbers.add(j+1)
                unique_numbers.add(k+1)
                if len(unique_numbers) == 3:
                    result.add(tuple(sorted((i+1, j+1, k+1))))
    print(strftime("%Y-%m-%d %H:%M:%S", gmtime()) + ' - done, ' +str(len(result))+ ' combinations.' )
    return len(result), result

# helper
def show_combinations(set, count):
    for i, val in enumerate(random.sample(set, count)):
        print (i, val)

# l8 = make_list(x8[1])
def make_list(set):
    return sorted(list(set))

# ll8 = change_tuples_to_lists(l8)
def change_tuples_to_lists(list_of_tuples):
    list_of_lists = []
    for tuple in list_of_tuples:
        list_of_lists += [list(tuple)]
    return list_of_lists;

# write_json(ll8, 'll8.json')
def write_json(object, filename):
    with open(filename, 'w') as f:
        json.dump(object, f, sort_keys=True)

# generate guess of 6 numbers (ordered)
def random_guess():
    guess=set()
    while len(guess) < 6:
        guess.add(random.randint(1, 37))
    return tuple(sorted(list(guess)))

# (1,2,3), (1,2,3,4,5,6)
def is_in_guess(triple, guess):
    triple_set=set(triple)
    return triple_set.issubset(guess)

def remove_known_triples(guesses, triples):
    guesses_set = set(guesses)
    filtered_triples = set(triples)
    for triple in triples:
        for guess in guesses:
            guess = tuple(sorted(guess))
            if is_in_guess(triple, guess):
                if triple in filtered_triples:
                    filtered_triples.remove(triple)
    return filtered_triples

def find_included_triples(guess):
    print(strftime("%Y-%m-%d %H:%M:%S", gmtime()) + ' - generating 20 sorted triples from guess: ' +str(guess)+ ' .')
    result=set()
    for i in range(6):
        for j in range(6):
            if j==i: break
            for k in range(6):
                if k==i or k==j: break
                unique_numbers = set()
                unique_numbers.add(g[i])
                unique_numbers.add(g[j])
                unique_numbers.add(g[k])
                if len(unique_numbers) == 3:
                    result.add(tuple(sorted((g[i], g[j], g[k]))))
    print(strftime("%Y-%m-%d %H:%M:%S", gmtime()) + ' - done, ' +str(len(result))+ ' combinations.' )
    return len(result), result

# mutates the triples set
def build_guess(triples):
    guess = set()
    while len(guess) < 6:
        triple = triples.pop()
        for number in triple:
            if len(guess) >= 6:
                break
            guess.add(number)
    return tuple(sorted(guess))







# test number of guesses if appears in set
def test(number_of_guesses, result_set, show_guesses=False):
    print('generating {} gueses for testing against set of {} entries.'.format(number_of_guesses, len(result_set)))
    guesses_list = []
    results = []
    for x in range(number_of_guesses):
        guesses_list += [random_guess()]
    for guess in guesses_list:
        results.append((guess, guess in result_set))
        if show_guesses:
            print ('guess: {}\t exists in set: {}'.format(guess, guess in result_set))
    print ('results summary:')
    print ('total guesses requested: {}'.format(len(guesses_list)))
    print ('total guesses tested: {}'.format(len(results)))
    hits = [ r for r in results if r[1] ]
    misses = [ r for r in results if not r[1] ]
    print ('total hits: {}'.format(len(hits)))
    print ('total misses: {}'.format(len(misses)))



def main():

    # creating all triples
    print(strftime("%Y-%m-%d %H:%M:%S", gmtime()) + ' - starting execution.')
    all_triples = fast_combination_set3(37)[1]
    triples = all_triples.copy()

    print ('length before: ' + str(len(triples)))
    triples = remove_known_triples(guesses_list, triples)
    print('length after: ' + str(len(triples)))

    g = random_guess()
    triples = remove_known_triples([g], triples)
    # 2nd time - no effect
    triples = remove_known_triples([g], triples)
    # unknown numbers - no effect
    triples = remove_known_triples([(44,45,56,78,88,97)], triples)
    print('length after remove 1 guesses triples : ' + str(len(triples)))

    new_guess = build_guess(triples)
    print('new guess: ' + str(new_guess))
    print('length after removing new guesses triples: ' + str(len(triples)))

    new_guess = build_guess(triples)
    print('new guess: ' + str(new_guess))
    print('length after removing new guesses triples: ' + str(len(triples)))

    new_guess = build_guess(triples)
    print('new guess: ' + str(new_guess))
    print('length after removing new guesses triples: ' + str(len(triples)))

    pass
    # x={1,2,3,4}
    # y = x.copy()
    #y = x
    # x.remove(2)
    # print (x,y)
    pass
    # make ordered list of tuples from the returned set
    print(strftime("%Y-%m-%d %H:%M:%S", gmtime()) + ' - converting set to ordered list.')
    l37 = make_list(x37[1])

    # change the inner types to lists
    print(strftime("%Y-%m-%d %H:%M:%S", gmtime()) + ' - converting inner tuples to lists.')
    ll37 = change_tuples_to_lists(l37)

    # write output to json file
    print(strftime("%Y-%m-%d %H:%M:%S", gmtime()) + ' - writing to file ll37.json .')
    write_json(ll37, 'll37.json')

    print(strftime("%Y-%m-%d %H:%M:%S", gmtime()) + ' - done.')

    # test 100000 random guesses
    print(strftime("%Y-%m-%d %H:%M:%S", gmtime()) + ' - test 100000 random guesses.')
    test(100000, s37)

# def main():
#
#     # creating all combination excluding all overlapping results
#     print(strftime("%Y-%m-%d %H:%M:%S", gmtime()) + ' - starting execution.')
#     x37=fast_combination_set6(37)
#
#     # just for easy reference when testing
#     s37=x37[1]
#
#     # make ordered list of tuples from the returned set
#     print(strftime("%Y-%m-%d %H:%M:%S", gmtime()) + ' - converting set to ordered list.')
#     l37 = make_list(x37[1])
#
#     # change the inner types to lists
#     print(strftime("%Y-%m-%d %H:%M:%S", gmtime()) + ' - converting inner tuples to lists.')
#     ll37 = change_tuples_to_lists(l37)
#
#     # write output to json file
#     print(strftime("%Y-%m-%d %H:%M:%S", gmtime()) + ' - writing to file ll37.json .')
#     write_json(ll37, 'll37.json')
#
#     print(strftime("%Y-%m-%d %H:%M:%S", gmtime()) + ' - done.')
#
#     # test 100000 random guesses
#     print(strftime("%Y-%m-%d %H:%M:%S", gmtime()) + ' - test 100000 random guesses.')
#     test(100000, s37)

main()
