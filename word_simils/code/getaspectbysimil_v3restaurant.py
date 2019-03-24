import gensim
import codecs
from operator import itemgetter
import numpy as np

def my_softmax(X):
    #X = np.array([1.1, 5.0, 2.8, 7.3])  # evidence for each choice
    theta = 1.0                         # determinism parameter

    ps = np.exp(X * theta)
    ps /= np.sum(ps)
    return ps 

def get_simis(ar_sentence , ref_word, negatives):
    simils_context = []
    simils = []
    for word in ar_sentence:
        #print(word)
        if word != '<unk>':
            try:
                res = model_r.most_similar(positive=[word, ref_word], negative=negatives)
                #print(res)
                tot = 0
                elems = 0
                for i,wt in enumerate(res):
                    try:
                        tot +=model_r.wv.similarity(w1=word, w2=wt[0])
                        elems+=1
                    except Exception as e:
                        print(e)
                simils_context.append(str(round(tot/(elems),4)))
                res1 = model_r.wv.similarity(w1=word, w2=ref_word)
                simils.append(str(round(res1,4)))
            except Exception as e:
                #print(e)
                #print('aqui '+ word)
                simils_context.append('0')
                simils.append('0')
        else:
            print('aqui '+word)
            simils_context.append('0')
            simils.append('0')
    return (simils_context, simils)
            #print(word+' -- '+ref_word)
            #print('similarity with context')
            #print(tot/(elems+1))

            #print('similarity without context')
            #res1 = model_r.wv.similarity(w1=word, w2=ref_word)
            #print(res1)

def get_simis_total(ar_sentence , ref_word, negatives):
    simils_context = []
    simils = []
    simils_total = []
    for word in ar_sentence:
        #print(word)
        if word != '<unk>':
            try:
                res = model_r.most_similar(positive=[word, ref_word], negative=negatives)
                #print(res)
                tot = 0
                elems = 0
                for i,wt in enumerate(res):
                    try:
                        tot +=model_r.wv.similarity(w1=word, w2=wt[0])
                        elems+=1
                    except Exception as e:
                        print(e)
                simils_context.append(str(round(tot/(elems),4)))
                res1 = model_r.wv.similarity(w1=word, w2=ref_word)
                simils.append(str(round(res1,4)))
                simils_total.append(str(round(tot/(elems) + res1, 4)))
            except Exception as e:
                #print(e)
                #print('aqui '+ word)
                simils_context.append('0')
                simils.append('0')
                simils_total.append('0')
        else:
            print('aqui '+word)
            simils_context.append('0')
            simils.append('0')
            simils_total.append('0')
    return (simils_context, simils, simils_total)


def get_simis_total_withdiff(ar_sentence, ar_sentence_diff , ref_word, negatives):
    simils_context = []
    simils = []
    simils_total = []
    for word, wdiff in zip(ar_sentence, ar_sentence_diff):
        #print(word)
        if word != '<unk>':
            try:
                res = model_r.most_similar(positive=[word, ref_word], negative=negatives)
                #print(res)
                tot = 0
                elems = 0
                for i,wt in enumerate(res):
                    try:
                        tot +=model_r.wv.similarity(w1=word, w2=wt[0])
                        elems+=1
                    except Exception as e:
                        print(e)
                #### aqui introduzco la importancia de la diferencia de vocabulario ###
                if(word != wdiff):
                    simils_context.append(str(round(tot/(elems),4)))
                    res1 = model_r.wv.similarity(w1=word, w2=ref_word)
                    simils.append(str(round(res1,4)))
                    simils_total.append(str(round(2*tot/(elems) + res1, 4)))
                    #print(str(round(2*tot/(elems) + res1, 4)))
                else:
                    simils_context.append(str(2*round(tot/(elems),4)))
                    res1 = model_r.wv.similarity(w1=word, w2=ref_word)
                    simils.append(str(round(res1,4)))
                    simils_total.append(str(2*round(2*tot/(elems) + res1, 4)))
                    #print(str(round(2*tot/(elems) + res1, 4)) + ' -- '+str(2*abs(round(2*tot/(elems) + res1, 4))))

            except Exception as e:
                #print(e)
                #print('aqui '+ word)
                simils_context.append('0')
                simils.append('0')
                simils_total.append('0')
        else:
            print('aqui '+word)
            simils_context.append('0')
            simils.append('0')
            simils_total.append('0')
    return (simils_context, simils, simils_total)

def negatives_2refwords(ref_words):
    s_ref_words = set(ref_words)
    simils = []
    for ref_word in ref_words:
        s_ref_word = set([ref_word])
        tocompair = s_ref_words-s_ref_word
        val_f = []
        for ref in tocompair:
            try:
                val = model_r.wv.similarity(w1=ref_word, w2=ref)
                val_f.append((ref, val))
            except Exception as e:
                print(e)
        simils.append(val_f)
    res = []
    for simil in simils:
        new = sorted(simil, key=itemgetter(1))       
        res.append(new[:2])

    resf = []
    for item in res:
        vals = [word for word, val in item]
        resf.append(vals)
            
    return resf 


def negatives_allrefwords(ref_words):
    s_ref_words = set(ref_words)
    simils = []
    resf = []
    for ref_word in ref_words:
        s_ref_word = set([ref_word])
        tocompair = s_ref_words-s_ref_word
        by_ref = ['great','even']
        for w in tocompair:
            by_ref.append(w)
        resf.append(by_ref)
    return  resf 

def negatives_refwords(ref_words):
    #the input refwords is a list of reference words
    #the output a list which consists of tuples with the two most unsimilirar words
    s_ref_words = set(ref_words)
    res = []
    for ref_word in ref_words:
        s_ref_word = set([ref_word])
        tocompair = s_ref_words-s_ref_word
        lower = 1
        unsimiliar_rw= ref_word 
        for ref in list(tocompair):
            #print(ref_word +' -- '+ref)
            try:
                val = model_r.wv.similarity(w1=ref_word, w2=ref)
                if(val<lower):
                    unsimilar_rw =ref
                    #print(unsimilar_rw)
                    lower = val 
                    #print(val)
            except Exception as e:
                print(e)
        aux = (ref_word, unsimilar_rw)
        res.append(aux)
    return res 

import time 
tinitial = time.time()
model_r = gensim.models.KeyedVectors.load_word2vec_format('/home/danny/git_imp/simil_words_final/models/restaurant.txt', binary=False)


#sentence = 'usually,order,wine,indian,ca,comment,wine,list,wine'
#ar_sentence = sentence.split(',')
#sentence = 'staff,friendliest,competent,<unk>,service,everything,else,place,make'
#ar_sentence = sentence.split(',')

lines_rest = []
lines_rest_withdiff = []
with open('../data/test/test_restaurant.txt') as f_r:
#with open('../data/ex.txt') as f_r:
    lines_rest = f_r.readlines()

#with open('../../differ_words/diff_data/test_r.txt') as f_rwd:
#    lines_rest_withdiff = f_rwd.readlines()

#ref_words = ['food','staff','price','ambience']
ref_words = ['food','staff','ambience']
##uncoment this to base other result
#neg_by_word = negatives_2refwords(ref_words)
#commnet this to base other result
neg_by_word = negatives_allrefwords(ref_words)


simils_by_ref = []
for i,ref_word in enumerate(ref_words):
    negatives_r = neg_by_word[i][::-1]
    out = codecs.open('../simils_rest/'+ref_word+'.txt','w', 'utf-8')
    out_probs = codecs.open('../probs_rest/'+ref_word+'.txt','w', 'utf-8')
    print('ref_word : ' + ref_word)
    #print(ref_word)
    print(negatives_r)
    simil_ref = []
    for line in lines_rest:
        #print(line_withdiff)
        ar_sentence_l = line.strip().split(' ') 
        #ar_sentence_l_withdiff = line_withdiff.strip().split(' ') 
        #print(str(len(ar_sentence_l)) +' -- ' +str(len(ar_sentence_l_withdiff)))
    
        ###########    
        ##uncoment this to base other result
        #simils_context, simils, simils_total = get_simis_total_withdiff(ar_sentence_l, ar_sentence_l_withdiff,ref_word, [negatives_r[0], negatives_r[1],'great', 'even'])

        ##coment this to base other result
        simils_context, simils, simils_total = get_simis_total(ar_sentence_l,ref_word, negatives_r)

        ######## write values
        out.write(' '.join(ar_sentence_l)+'\n')
        out.write(' '.join(simils_context) +'\n')
        out.write(' '.join(simils)+'\n')
        out.write(' '.join(simils_total)+ '\n')

        ######## write probs
        aux_soft = my_softmax(np.array([float(v) for v in simils_total]))
        line_prob = [str(round(x,4)) for x in aux_soft]
        
        out_probs.write(' '.join(ar_sentence_l)+'\n')
        out_probs.write(' '.join(line_prob)+'\n')

        simil_ref.append(simils_total)
    simils_by_ref.append(simil_ref)

#### Total Values ###
total = []
for j in range(len(simils_by_ref[0])):
    aux =[]
    for i in range(len(ref_words)):
        simils_by_ref[i][j]
        if(i == 0):
            aux = [float(val) for val in simils_by_ref[i][j]]
        else:
            aux = [a+float(val) for a, val in zip(aux, simils_by_ref[i][j])]
    #print(aux)
    #get softmax values
    aux_soft = my_softmax(np.array(aux))
    total.append([str(round(x,4)) for x in aux_soft])

out_total = codecs.open('../simils_rest/total_simils_rest.txt', 'w','utf-8')
for k,line in enumerate(lines_rest):
    out_total.write(line)
    out_total.write(' '.join(total[k])+'\n')

tfinal = time.time()
print("the similarity as attention mechanism takes")
print(tfinal-tinitial)

