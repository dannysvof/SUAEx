import codecs

def format_lines(attib_file):
    totales = []
    with open(attib_file, 'r') as f:
        lines = f.readlines()
    arr_letras = []
    arr_pesos = []
    for i in range(len(lines)):
        if(i%4==0):
            arr_letras.append(lines[i].strip().split(' '))
            #print(lines[i].strip())
        elif(i%4==3):
            pesos = lines[i].strip().split(' ')
            arr_pesos.append(pesos)
            float_vals = [float(val) for val in pesos]
            total = 0
            for x in float_vals:
                total+=x
            totales.append(total)
    return (arr_letras,arr_pesos, totales)

def sort_list(lista):
    indexs = sorted(range(len(lista)), key=lambda k: lista[k], reverse=True)
    return indexs 
    
f_attrib_weights_rf1 = '../word_simils/simils_rest/staff.txt'
f_attrib_weights_rf2 = '../word_simils/simils_rest/ambience.txt'
f_attrib_weights_rf3 = '../word_simils/simils_rest/food.txt'

(ar_letras_rf1, ar_pesos_rf1, totales_staff) = format_lines(f_attrib_weights_rf1)
(ar_letras_rf2, ar_pesos_rf2, totales_ambience) = format_lines(f_attrib_weights_rf2)
(ar_letras_rf3, ar_pesos_rf3, totales_food) = format_lines(f_attrib_weights_rf3)

#suaex_labels = codecs.open('test_labels_abae.txt','w')
suaex_labels = []
with open('../category_atribution/test_labels_abae.txt','r') as f:
    suaex_labels = f.readlines()

words_cat1 = set()
words_cat2 = set()
words_cat3 = set()

for letras, valores1, valores2, valores3, label in zip(ar_letras_rf1, ar_pesos_rf1, ar_pesos_rf2, ar_pesos_rf3, suaex_labels):
    label = label.strip()
    if label == "Staff":#usar los valores1
        ordered_indexs = sort_list(valores1)
        selected_words = [letras[ordered_indexs[0]]]
        words_cat1 =  words_cat1.union(set(selected_words))
    elif label == "Ambience":#usar los valores2
        ordered_indexs = sort_list(valores2)
        selected_words = [letras[ordered_indexs[0]]]
        words_cat2 =  words_cat2.union(set(selected_words))
    elif label == "Food":#usar los valores3
        ordered_indexs = sort_list(valores3)
        selected_words = [letras[ordered_indexs[0]]]
        words_cat3 =  words_cat3.union(set(selected_words))
    else:
        print("aq")

print("group 1 - Staff")
print(list(words_cat1)[:50])
print("group 2 - Ambience")
print(list(words_cat2)[:50])
print("group 3 - Food")
print(list(words_cat3)[:50])
