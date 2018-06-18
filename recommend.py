import json
from scipy import spatial
import nltk
from nltk.corpus import stopwords

data = json.load(open('courses.json', 'r'))

courses = list(data.keys())

courses_id_to_name = json.load(open('subjects.json', 'r'))

for course in courses:
    data[course] = [w.lower() for w in nltk.word_tokenize(data[course]['syllabus']) if w not in stopwords.words('english') and len(w)!=1]

import string

for course in courses:
    for word_ind in range(len(data[course])):
        for punct in string.punctuation + '•':
            data[course][word_ind] = data[course][word_ind].replace(punct, " ")

for course in courses:
    data[course] = " ".join(data[course]).split(" ")

to_del = []
for course_ind in range(len(courses)):
    if (len(data[courses[course_ind]]) < 5):
        print (courses[course_ind])
        to_del.append(course_ind)
        del data[courses[course_ind]]


to_del.reverse()

for index in to_del:
    del courses[index]


corpora = set()

for a in data:
    for b in data[a]:
        corpora.add(b)

corpora = list(corpora)
matrix = np.zeros((len(data), len(corpora)))

for course_ind in range(len(courses)):
    for word in data[courses[course_ind]]:
        matrix[course_ind][corpora.index(word)] = 1



normalised_mat = matrix - np.asarray([(np.mean(matrix, 1))]).T
A = normalised_mat.T / np.sqrt(matrix.shape[0] - 1)
U, S, V = np.linalg.svd(A)
del U
del S
del A
del normalised_mat

sliced = V.T[:,:100]

len(sliced)


def find_top_k(to_find_sim, sliced, k, different_dep = False):
    top_k = []
    max_r = 0
    for course_ind in range(len(courses)):
        if (different_dep == True):
            if (courses[to_find_sim][0:2] == courses[course_ind][0:2]):
                continue
        if (course_ind != to_find_sim):
            result = 1 - spatial.distance.cosine(sliced[course_ind], sliced[to_find_sim])
            if (len(top_k) < k):
                top_k.append([result, courses[course_ind]])
            else:
                top_k = sorted(top_k, reverse = True)
                if (top_k[-1][0] < result):
                    top_k[-1] = [result, courses[course_ind]]
    return top_k


def find_top_k_vec(vec, sliced, k):
    top_k = []
    max_r = 0
    for course_ind in range(len(courses)):
        result = 1 - spatial.distance.cosine(sliced[course_ind], vec)
        if (len(top_k) < k):
            top_k.append([result, courses[course_ind]])
        else:
            top_k = sorted(top_k, reverse = True)
            if (top_k[-1][0] < result):
                top_k[-1] = [result, courses[course_ind]]
    return top_k


def print_top_k(course_name, sliced, k, print_=True, different_dep = False):
    tmp = find_top_k(courses.index(course_name), sliced, 5, different_dep)
    for i in range(len(tmp)):
        if (tmp[i][1] in courses_id_to_name):
            tmp[i][1] = tmp[i][1] + " - " + courses_id_to_name[tmp[i][1]]
    if (print_):
        this_name = ""
        if (course_name in courses_id_to_name):
            this_name = courses_id_to_name[course_name]
        print ("Most similar courses to ", course_name, " ", this_name)
        pprint (tmp)
    return tmp

def print_top_k_vec(vec, sliced, k, print_=True):
    tmp = find_top_k_vec(vec, sliced, 5)
    for i in range(len(tmp)):
        if (tmp[i][1] in courses_id_to_name):
            tmp[i][1] = tmp[i][1] + " - " + courses_id_to_name[tmp[i][1]]
    if (print_):
        this_name = ""
        print ("Most similar courses are ")
        pprint (tmp)
    return tmp



print_top_k('MA21007', sliced, 5)
print_top_k('CS11001', sliced, 5)

def vec(course_name, sliced):
    return sliced[courses.index(course_name)]

v_m = vec('HS20001', sliced)
v_c = vec('EP60008', sliced)
v = (v_c-v_m)/2


print_top_k('IM21003', sliced, 5, different_dep = True)
