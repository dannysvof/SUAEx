import gensim
import json
import codecs

#load model
model = gensim.models.KeyedVectors.load_word2vec_format('/home/danny/gpuimp/post_abae_mymodel1_similwords/model_200_abae.txt', binary=False)

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

def mayor3(x,y,z):
    mayor = -1
    index = -1
    if(x>mayor):
        mayor=x
        index = 0
    if(y>mayor):
        mayor=y
        index = 1
    if(z>mayor):
        mayor=z
        index = 2

    return (mayor, index)

################ Evaluation ####################################
from sklearn.metrics import classification_report

def evaluation(true, predict, domain):
    true_label = []
    predict_label = []

    if domain == 'restaurant':
        for line in predict:
            predict_label.append(line.strip())
        for line in true:
            true_label.append(line.strip())
        
        print(classification_report(true_label, predict_label, ['Food', 'Staff', 'Ambience', 'Anecdotes', 'Price', 'Miscellaneous'], digits=3))


#print('ok')
#f_attrib_weights = '/home/danny/gpuimp/experiments/modified_abae_v3_mymodel/code/output_dir_mymodel/restaurant/att_weights'

f_attrib_weights_rf1 = '../word_simils/simils_rest/staff.txt'
f_attrib_weights_rf2 = '../word_simils/simils_rest/ambience.txt'
f_attrib_weights_rf3 = '../word_simils/simils_rest/food.txt'

(ar_letras_rf1, ar_pesos_rf1, totales_staff) = format_lines(f_attrib_weights_rf1)
(ar_letras_rf2, ar_pesos_rf2, totales_ambience) = format_lines(f_attrib_weights_rf2)
(ar_letras_rf3, ar_pesos_rf3, totales_food) = format_lines(f_attrib_weights_rf3)

print(len(totales_staff))
print(totales_staff[0])
print(totales_ambience[0])
print(totales_food[0])

predict_labels = []
#open the refwords and assigns the greater one to each sentence

out_labels = codecs.open('test_labels_abae.txt','w','utf-8')

for (val1,val2,val3) in zip(totales_staff, totales_ambience, totales_food):
    #print(str(val1) +' -- '+  str(val2) + ' -- ' + str(val3))
    (_, index) = mayor3(val1, val2, val3)
    if index==0:
        out_labels.write('Staff\n')
        predict_labels.append('Staff')
    elif index==1:
        out_labels.write('Ambience\n')
        predict_labels.append('Ambience')
    elif index==2:
        out_labels.write('Food\n')
        predict_labels.append('Food')
   

#domain = 'restaurant'
#print(len(predict_labels))
#test_labels = '/home/danny/gpuimp/experiments/modified_abae/preprocessed_data/%s/test_label.txt' % (domain)
#print(open(test_labels))

domain = 'restaurant'
print('--- Results on %s domain ---' % (domain))
test_labels = '/home/danny/gpuimp/experiments/modified_abae/preprocessed_data/%s/test_label.txt' % (domain)
evaluation(open(test_labels), predict_labels, domain)

