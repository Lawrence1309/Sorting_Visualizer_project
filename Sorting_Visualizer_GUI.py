from math import ceil, log2, floor, log10
import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from tkinter import *


def bubble_sort(list):
    for i in range(len(list)):
        for j in range(len(list)):
            if j == len(list) - 1:
                break
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                yield list


def count_sort(list):
    maxi = max(list)
    aux = [0] * (maxi + 1)

    for i in list:
        aux[i] += 1

    k = 0
    for i in range(len(aux)):
        if aux[i] != 0:
            for j in range(aux[i]):
                list[k] = i
                yield list
                k += 1


def heap_sort(list, last_index):
    if last_index > 0:
        new_list = []
        new_list.clear()
        new_list = list[:last_index]
        unsorted_fam = 0
        sorted_array = False
        while (not sorted_array):
            new_list.clear()
            new_list = list[:last_index]
            if ceil(((len(new_list) - 1) - 1) / 2) == floor(((len(new_list) - 1) - 1) / 2):
                var = -1
                if new_list[-1] > new_list[((len(new_list) - 1) - 1) // 2]:
                    list[last_index - 1], list[((len(new_list) - 1) - 1) // 2] = list[((len(new_list) - 1) - 1) // 2], \
                                                                                 list[last_index - 1]
                    yield list
            else:
                var = 1

            check_fam = unsorted_fam
            for i in range(len(new_list) - 2, 0, -2):
                new_list.clear()
                new_list = list[:last_index]
                if new_list[i] > new_list[(i - 1) // 2] or new_list[i + var] > new_list[(i - 1) // 2]:
                    if new_list[i] > new_list[i + var]:
                        list[i], list[(i - 1) // 2] = list[(i - 1) // 2], list[i]
                        yield list
                    else:
                        list[i + var], list[(i - 1) // 2] = list[(i - 1) // 2], list[i + var]
                        yield list
                else:
                    unsorted_fam -= 1

            if check_fam == unsorted_fam + ((len(new_list) - 1) // 2):
                list[0], list[last_index - 1] = list[last_index - 1], list[0]
                yield list
                sorted_array = True
        last_index -= 1
        yield from heap_sort(list, last_index)


def insertion_sort(list):
    for i in range(len(list)):
        for j in range(i, 0, -1):
            if list[j] < list[j - 1]:
                list[j], list[j - 1] = list[j - 1], list[j]
                yield list
            else:
                break


def merge_sort(list, start, end):
    if end != start:
        mid = (end + start) // 2

        yield from merge_sort(list, start, mid)
        yield from merge_sort(list, mid + 1, end)  # 'start' index of 2nd half is from mid+1

        i = j = k = 0
        temp_list = list.copy()
        for k in range(end - start + 1):
            if i == (mid - start + 1):
                list[start + k] = temp_list[mid + 1 + j]
                j += 1
                yield list
                continue
            if j == (end - mid):
                list[start + k] = temp_list[start + i]
                i += 1
                yield list
                continue
            if temp_list[start + i] < temp_list[mid + 1 + j]:
                list[start + k] = temp_list[start + i]
                i += 1
                yield list
                continue
            if temp_list[start + i] >= temp_list[mid + 1 + j]:
                list[start + k] = temp_list[mid + 1 + j]
                j += 1
                yield list
                continue

        yield list


def quick_sort(list, low, high):
    if low < high:
        i = 0
        reverse_found = False
        forward_found = False
        reverse_loop = range(high, low - 1, -1)
        piv = list[high]
        piv_index = high
        reverse_index = reverse_loop[i + 1]
        for forward_index in range(low, high):
            if list[forward_index] >= piv:
                forward_found = True
            if reverse_found is not True:
                for reverse_index in range(reverse_loop[i + 1], low - 1, -1):
                    i += 1
                    if reverse_index + 1 == forward_index:
                        break
                    if list[reverse_index] < piv:
                        reverse_found = True
                        break
                    if forward_index == reverse_index:
                        break

            if forward_index < reverse_index:
                if forward_found is True and reverse_found is True:
                    list[forward_index], list[reverse_index] = list[reverse_index], list[forward_index]
                    yield list
                    forward_found = False
                    reverse_found = False
            else:
                if forward_found is True and reverse_found is not True:
                    list[piv_index], list[forward_index] = list[forward_index], list[piv_index]
                    yield list
                    piv_index = forward_index
                    break
                if forward_found is not True and reverse_found is True:
                    list[piv_index], list[reverse_index + 1] = list[reverse_index + 1], list[piv_index]
                    yield list
                    piv_index = reverse_index + 1
                    break
        yield from quick_sort(list, low, piv_index - 1)
        yield from quick_sort(list, piv_index + 1, high)


def radix_sort(list, digit, max_num):
    new_list = []
    new_list.clear()
    new_list = list.copy()
    if digit == 0.1:
        digit = digit * 10
    if (10 ** max_num) >= digit:
        for i in range(len(new_list)):
            new_list[i] = int((new_list[i] / digit) % 10)

        k = 0
        for i in range(10):
            for j in range(k, len(new_list)):
                if new_list[j] == i:
                    list.insert(k, list[j])
                    list.pop(j + 1)
                    yield list
                    new_list.insert(k, list[j])
                    new_list.pop(j + 1)
                    k += 1

        digit = digit * 10
        yield from radix_sort(list, digit, max_num)


def selection_sorting(list):
    last_index = len(list)
    for i in range(len(list)):
        big_num = list[0]
        last_index -= 1
        for j in range(last_index + 1):
            if big_num < list[j]:
                big_num = list[j]
            if j == last_index:
                list[list.index(big_num)], list[last_index] = list[last_index], list[list.index(big_num)]
                yield list




if __name__ == "__main__":
    root = Tk()
    root.geometry('180x300')
    root.configure(bg='tomato')

    e = Entry(root,borderwidth=5,font='Tahoma 9 italic')
    e.insert(0,'Elements: ')
    e.grid(row=0,column=4)

    list_num = []
    max_num = 0

    methods = ['Bubble Sorting',
               'Counting Sorting',
               'Heap Sorting',
               'Insertion Sorting',
               'Merge Sorting',
               'Quick Sorting',
               'Radix Sorting',
               'Selection Sorting']
    method = StringVar()
    method.set(methods[0])
    title = 'Bubble sort'

    for i in range(8):
        rb1 = Radiobutton(root, text=methods[i], variable=method, value=methods[i],bg='gold',width=14,font='Tahoma 10 bold')
        rb1.grid(row=i+1,column=4,padx=10)

    def begin_process(value):
        global generator,title,method,list_num,max_num,N
        number = e.get()
        number = number[len('Elements: '):]
        if number.isdigit():
            N = int(number)
            random.seed(time.time())
            list_num = [random.randrange(1, 100) for j in range(N)]
            max_num = max(list_num)
            max_num = int(log10(max_num)) + 1
        Label(root, text='The process shall begin with '+str(value))
        if value == "Bubble Sorting":
            title = "Bubble sort"
            generator = bubble_sort(list_num)
        elif value == "Counting Sorting":
            title = "Counting sort"
            generator = count_sort(list_num)
        elif value == "Heap Sorting":
            title = "Heap sort"
            generator = heap_sort(list_num, len(list_num))
        elif value == "Insertion Sorting":
            title = "Insertion Sorting"
            generator = insertion_sort(list_num)
        elif value == "Merge Sorting":
            title = "Merge sort"
            generator = merge_sort(list_num, 0, len(list_num) - 1)
        elif value == "Quick Sorting":
            title = "Quick sort"
            generator = quick_sort(list_num, 0, len(list_num) - 1)
        elif value == "Radix Sorting":
            title = "Radix sort"
            generator = radix_sort(list_num, 0.1, max_num)
        elif value == "Selection Sorting":
            title = "Selection sort"
            generator = selection_sorting(list_num)
        graph_it()

    Button(root, text='Begin', command=lambda:begin_process(method.get()),font = 'Tahoma 10 bold', bg = 'darkslategray').grid(row=11,column=4)


    def graph_it():
        global text,fig,bar_rects,title,anim,generator,ax
        plt.style.use('Solarize_Light2')
        fig, ax = plt.subplots()
        ax.set_title(title)
        bar_rects = ax.bar(range(len(list_num)), list_num, align="edge")
        ax.set_xlim(0, N)
        ax.set_ylim(0, (1.07 * 100))
        ax.set_xlabel('Number of elements')
        ax.set_ylabel('Value')
        text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
        iteration = [0]
        anim = animation.FuncAnimation(fig, func=update_fig,
                                       fargs=(bar_rects, iteration), frames=generator, interval=1,
                                       repeat=False)
        plt.show()

    def update_fig(list_num, rects, iteration):
        for rect, val in zip(rects, list_num):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text("Number of operations: {}".format(iteration[0]))

    root.mainloop()

