#!/usr/bin/python3

import random
import json
from time import gmtime, strftime

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
    triple_as_set = set(triple)
    return triple_as_set.issubset(guess)



def remove_known_triples(guess, triples):
    for triple in triples:
        if is_in_guess(triple, guess):
            triples.remove(triple)






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

    # creating all combination excluding all overlapping results
    print(strftime("%Y-%m-%d %H:%M:%S", gmtime()) + ' - starting execution.')
    x37=fast_combination_set6(37)

    # just for easy reference when testing
    s37=x37[1]

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

main()
