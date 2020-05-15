from math import ceil,log2,floor,log10
import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation



def bubble_sort(list):
    for i in range(len(list)):
        for j in range(len(list)):
            if j == len(list) - 1:
                break
            if list[j] > list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]
                yield list


def count_sort(list):
    maxi = max(list)
    aux = [0]*(maxi+1)

    for i in list:
        aux[i] += 1

    k = 0
    for i in range(len(aux)):
        if aux[i] != 0:
            for j in range(aux[i]):
                list[k] = i
                yield list
                k += 1


def heap_sort(list,last_index):
    if last_index > 0:
        new_list = []
        new_list.clear()
        new_list = list[:last_index]
        unsorted_fam = 0
        sorted_array = False
        while(not sorted_array):
            new_list.clear()
            new_list = list[:last_index]
            if ceil(((len(new_list)-1)-1)/2) == floor(((len(new_list)-1)-1)/2):
                var = -1
                if new_list[-1] > new_list[((len(new_list)-1)-1)//2]:
                    list[last_index-1],list[((len(new_list)-1)-1)//2] = list[((len(new_list)-1)-1)//2],list[last_index-1]
                    yield list
            else:
                var = 1

            check_fam = unsorted_fam
            for i in range(len(new_list)-2,0,-2):
                new_list.clear()
                new_list = list[:last_index]
                if new_list[i] > new_list[(i-1)//2] or new_list[i+var] > new_list[(i-1)//2]:
                    if new_list[i] > new_list[i+var]:
                        list[i],list[(i-1)//2] = list[(i-1)//2],list[i]
                        yield list
                    else:
                        list[i+var], list[(i-1)//2] = list[(i-1)//2], list[i+var]
                        yield list
                else:
                    unsorted_fam -= 1

            if check_fam == unsorted_fam + ((len(new_list)-1)//2):
                list[0],list[last_index-1] = list[last_index-1],list[0]
                yield list
                sorted_array = True
        last_index -= 1
        yield from heap_sort(list,last_index)



def insertion_sort(list):
    for i in range(len(list)):
        for j in range(i, 0, -1):
            if list[j] < list[j - 1]:
                list[j], list[j - 1] = list[j - 1], list[j]
                yield list
            else:
                break



def merge_sort(list,start,end):
    if end != start:
        mid = (end+start)//2

        yield from merge_sort(list,start,mid)
        yield from merge_sort(list,mid+1,end)              # 'start' index of 2nd half is from mid+1

        i = j = k =0
        temp_list = list.copy()
        for k in range(end-start+1):
            if i == (mid-start+1):
                list[start+k] = temp_list[mid+1+j]
                j += 1
                yield list
                continue
            if j == (end-mid):
                list[start+k] = temp_list[start+i]
                i += 1
                yield list
                continue
            if temp_list[start+i] < temp_list[mid+1+j]:
                list[start+k] = temp_list[start+i]
                i += 1
                yield list
                continue
            if temp_list[start+i] >= temp_list[mid+1+j]:
                list[start+k] = temp_list[mid+1+j]
                j += 1
                yield list
                continue

        yield list





def quick_sort(list,low,high):
    if low<high:
        i = 0
        reverse_found = False
        forward_found = False
        reverse_loop = range(high, low-1, -1)
        piv = list[high]
        piv_index = high
        reverse_index = reverse_loop[i + 1]
        for forward_index in range(low,high):
            if list[forward_index] >= piv:
                forward_found = True
            if reverse_found is not True:
                for reverse_index in range(reverse_loop[i+1],low-1,-1):
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
                    list[forward_index],list[reverse_index] = list[reverse_index],list[forward_index]
                    yield list
                    forward_found = False
                    reverse_found = False
            else:
                if forward_found is True and reverse_found is not True:
                    list[piv_index],list[forward_index] = list[forward_index],list[piv_index]
                    yield list
                    piv_index = forward_index
                    break
                if forward_found is not True and reverse_found is True:
                    list[piv_index],list[reverse_index+1] = list[reverse_index+1],list[piv_index]
                    yield list
                    piv_index = reverse_index+1
                    break
        yield from quick_sort(list,low,piv_index-1)
        yield from quick_sort(list,piv_index+1,high)




def radix_sort(list,digit,max_num):
    new_list = []
    new_list.clear()
    new_list = list.copy()
    if digit == 0.1:
        digit = digit*10
    if (10**max_num) >= digit:
        for i in range(len(new_list)):
            new_list[i] = int((new_list[i]/digit)%10)

        k=0
        for i in range(10):
           for j in range(k,len(new_list)):
               if new_list[j] == i:
                   list.insert(k,list[j])
                   list.pop(j+1)
                   yield list
                   new_list.insert(k, list[j])
                   new_list.pop(j + 1)
                   k += 1


        digit = digit*10
        yield from radix_sort(list,digit,max_num)




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
    N = int(input('Please enter the number of elements: '))
    method = input('Here are the following choices:\na) Bubble sorting\nb) Counting Sorting\nc) Heap Sorting'
                   '\nd) Insertion Sorting\ne) Merge Sorting\nf) Quick Sorting\ng) Radix Sorting\nh) Selection Sorting\nYour choice is: ')

    random.seed(time.time())
    list = [random.randrange(1, 100) for i in range(N)]

    # for radix
    max_num = max(list)
    max_num = int(log10(max_num)) + 1

    if method == "a":
        title = "Bubble sort"
        generator = bubble_sort(list)
    elif method == "b":
        title = "Counting sort"
        generator = count_sort(list)
    elif method == "c":
        title = "Heap sort"
        generator = heap_sort(list,len(list))
    elif method == "d":
        title = "Insertion Sorting"
        generator = insertion_sort(list)
    elif method == "e":
        title = "Merge sort"
        generator = merge_sort(list,0,len(list)-1)
    elif method == "f":
        title = "Quick sort"
        generator = quick_sort(list,0,len(list)-1)
    elif method == "g":
        title = "Radix sort"
        generator = radix_sort(list,0.1,max_num)
    elif method == "h":
        title = "Selection sort"
        generator = selection_sorting(list)


    def update_fig(list, rects, iteration,text):
        for rect, val in zip(rects, list):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text("Number of operations: {}".format(iteration[0]))



    plt.style.use('Solarize_Light2')
    fig, axs = plt.subplots(2,4,figsize = (10,10))
    fig.tight_layout(pad=6.0)
    iteration = [0]
    anim = []

    def run_algo(list,fig,index_row,index_col,axs,title):
        list_1 = list.copy()
        axs[index_row][index_col].set_title(title)
        bar_rects = axs[index_row][index_col].bar(range(len(list_1)), list_1, align="edge")
        axs[index_row][index_col].set_xlim(0, N)
        axs[index_row][index_col].set_ylim(0, (1.07 * 100))
        axs[index_row][index_col].set_xlabel('Number of elements')
        axs[index_row][index_col].set_ylabel('Value')
        text = axs[index_row][index_col].text(0.02, 0.95, "", transform=axs[index_row][index_col].transAxes)

        iteration_1 = iteration.copy()

        if index_row == 0 and index_col == 0:
            anim.append(animation.FuncAnimation(fig, func=update_fig,
                                       fargs=(bar_rects, iteration_1,text), frames = bubble_sort(list_1), interval=5,
                                       repeat=False))
        if index_row == 0 and index_col == 1:
            anim.append(animation.FuncAnimation(fig, func=update_fig,
                                                fargs=(bar_rects, iteration_1,text), frames=count_sort(list_1), interval=5,
                                                repeat=False))
        if index_row == 0 and index_col == 2:
            anim.append(animation.FuncAnimation(fig, func=update_fig,
                                                fargs=(bar_rects, iteration_1,text), frames=heap_sort(list_1,len(list_1)), interval=5,
                                                repeat=False))
        if index_row == 0 and index_col == 3:
            anim.append(animation.FuncAnimation(fig, func=update_fig,
                                                fargs=(bar_rects, iteration_1,text), frames=insertion_sort(list_1), interval=5,
                                                repeat=False))
        if index_row == 1 and index_col == 0:
            anim.append(animation.FuncAnimation(fig, func=update_fig,
                                                fargs=(bar_rects, iteration_1,text), frames=merge_sort(list_1,0,len(list_1)-1), interval=5,
                                                repeat=False))
        if index_row == 1 and index_col == 1:
            anim.append(animation.FuncAnimation(fig, func=update_fig,
                                                fargs=(bar_rects, iteration_1,text), frames=quick_sort(list_1,0,len(list_1)-1), interval=5,
                                                repeat=False))
        if index_row == 1 and index_col == 2:
            anim.append(animation.FuncAnimation(fig, func=update_fig,
                                                fargs=(bar_rects, iteration_1,text), frames=radix_sort(list_1,0.1,max_num), interval=5,
                                                repeat=False))
        if index_row == 1 and index_col == 3:
            anim.append(animation.FuncAnimation(fig, func=update_fig,
                                                fargs=(bar_rects, iteration_1,text), frames=selection_sorting(list_1), interval=5,
                                                repeat=False))
        # axs[1].set_title(title)
        # bar_rects_1 = axs[1].bar(range(len(list_1)), list_1, align="edge")
        # axs[1].set_xlim(0, N)
        # axs[1].set_ylim(0, (1.07 * 100))
        # axs[1].set_xlabel('Number of elements')
        # axs[1].set_ylabel('Value')
        # iteration_1 = [0]
        # # text = axs[1].text(0.02, 0.95, "", transform=axs[0].transAxes)
        # anim1 = animation.FuncAnimation(fig, func=update_fig,
        #                                fargs=(bar_rects_1, iteration_1), frames=count_sort(list_1), interval=1,
        #                                repeat=False)
    # run_algo(list,0,generator)
    run_algo(list,fig,0,0,axs,'Bubble Sort')
    run_algo(list,fig,0,1,axs,'Counting Sort')
    run_algo(list,fig,0,2,axs,'Heap Sort')
    run_algo(list,fig,0,3,axs,'Insertion Sort')
    run_algo(list,fig,1,0,axs,'Merge Sort')
    run_algo(list,fig,1,1,axs,'Quick Sort')
    run_algo(list,fig,1,2,axs,'Radix Sort')
    run_algo(list,fig,1,3,axs,'Selection Sort')

    plt.show()

    # zipper = zip(bar_rects,list)
    # a,b = zip(*zipper)
    # print(b)





