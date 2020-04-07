nb_lines = int(input())

presentation_sentence = lambda name, age, weight, nationality : print("{} is a {} {} and weighs {} kg.".format(name, age, nationality, weight))

print("let's present some guys!")
input()

list_features = []
for _ in range(nb_lines):
    list_features = (input().split("/"))
    presentation_sentence(list_features[0], list_features[1], list_features[2], list_features[3])

        





