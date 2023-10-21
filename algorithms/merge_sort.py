import pygame_visualizer as pv

def merge_sort(draw_info, ascending=True):
    lst = draw_info.lst
    def merge(nums, start, mid, end):
        temp = []
        i, j = start, mid + 1
        while i <= mid and j <= end:
            if nums[i] < nums[j] and ascending or nums[i] > nums[j] and not ascending:
                temp.append(nums[i])
                i += 1
            else:
                temp.append(nums[j])
                j += 1
            pv.draw_list(draw_info, {i: draw_info.GREEN}, True)
            yield True

        while i <= mid:
            temp.append(nums[i])
            i += 1
            pv.draw_list(draw_info, {i: draw_info.GREEN}, True)
            yield True
        while j <= end:
            temp.append(nums[j])
            j += 1
            pv.draw_list(draw_info, {i: draw_info.GREEN}, True)
            yield True
        nums[start:end + 1] = temp


        return nums

    def mergeSort(lst, start, end,ascending=True):
        if start >= end:
            return
        else:
            mid = start + (end - start) // 2
            yield from mergeSort(lst, start, mid, ascending)
            yield from mergeSort(lst, mid + 1, end, ascending)
            yield from merge(lst, start, mid, end)
    yield from mergeSort(lst, 0, len(lst) - 1)
    return lst