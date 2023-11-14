from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

sys.path.append("../2022-cs-65dsamidproject")

import sortingAlgorithms as sort_algo
import searchingAlgorithms as search_algo


class VideoTableModel(QAbstractTableModel):
    def __init__(self, data, header, parent=None):
        super(VideoTableModel, self).__init__(parent)
        self._data = data
        self._header = header
        self._original_data = data

    def rowCount(self, parent=QModelIndex()):
        return len(self._data)

    def columnCount(self, parent=QModelIndex()):
        return len(self._header)

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            video = self._data[index.row()]
            if index.column() == 0:
                return video.URL
            elif index.column() == 1:
                return video.Channel
            elif index.column() == 2:
                return video.Subscribers
            elif index.column() == 3:
                return video.Title
            elif index.column() == 4:
                return video.Likes
            elif index.column() == 5:
                return video.Duration
            elif index.column() == 6:
                return video.Views
            elif index.column() == 7:
                return video.Comments
        return QVariant()

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self._header[section]
        return QVariant()

    def sort_by(self, start, end, attribute, algo, order: bool):
        key_function = lambda x: getattr(x, attribute)
        if algo == "Bubble Sort":
            sort_algo.bubble_sort(
                self._data,
                start=start,
                end=end,
                key=key_function,
            )
        elif algo == "Insertion Sort":
            sort_algo.insertion_sort(
                self._data,
                start=start,
                end=end,
                key=key_function,
            )
        elif algo == "Selection Sort":
            sort_algo.selection_sort(
                self._data,
                start=start,
                end=end,
                key=key_function,
            )
        elif algo == "Merge Sort":
            sort_algo.merge_sort(
                self._data,
                start=start,
                end=end,
                key=key_function,
            )
        elif algo == "Quick Sort":
            sort_algo.quick_sort(
                self._data,
                start=start,
                end=end,
                key=key_function,
            )
        elif algo == "Heap Sort":
            sort_algo.heap_sort(
                self._data,
                start=start,
                end=end,
                key=key_function,
            )
        elif algo == "Brick Sort":
            sort_algo.even_odd_sort(
                self._data,
                start=start,
                end=end,
                key=key_function,
            )
        elif algo == "Radix Sort":
            sort_algo.radix_sort(
                self._data,
                start=start,
                end=end,
                key=key_function,
            )
        elif algo == "Counting Sort":
            sort_algo.count_sort(
                self._data,
                start=start,
                end=end,
                key=key_function,
            )
        elif algo == "Bucket Sort":
            sort_algo.bucket_sort(
                self._data,
                start=start,
                end=end,
                key=key_function,
            )
        elif algo == "PigeonHole Sort":
            sort_algo.pigeonhole_sort(
                self._data,
                start=start,
                end=end,
                key=key_function,
            )
        elif algo == "Bead Sort":
            sort_algo.bead_sort(
                self._data,
                start=start,
                end=end,
                key=key_function,
            )
        if order == False:
            self._data.reverse()
        self.layoutChanged.emit()

    def multi_lvl_sort(self, start, end, attributes, algo, order: bool):
        self.sort_by(start, end, attributes[0], algo, order)
        ranges = self.find_same_attribute_ranges(attributes[0])
        for i in range(1, len(attributes)):
            for start, end in ranges:
                self.sort_by(start, end, attributes[i], algo, order)
            ranges = self.find_same_attribute_ranges(attributes[i])

    def reset_data(self, data):
        self._data = data
        self.layoutChanged.emit()

    def find_same_attribute_ranges(self, attribute):
        ranges = []
        current_range = [0, 0]
        current_value = getattr(self._data[0], attribute)

        for i, item in enumerate(self._data):
            if getattr(item, attribute) == current_value:
                current_range[1] = i
            else:
                ranges.append(tuple(current_range))
                current_range = [i, i]
                current_value = getattr(item, attribute)

        # Append the last range
        ranges.append(tuple(current_range))

        return ranges

    def search_by(self, start, end, algo, target, filter, key):
        key_function = lambda x: getattr(x, key)
        result = []
        if algo == "Linear Search":
            result = search_algo.linearSearch(
                self._data, 0, end, target, filter, key_function
            )
        elif algo == "Jump Search":
            self.data = self.sort_by(start, end, key, "Merge Sort", True)
            result = search_algo.jump_search(
                self.data, start, end, target, filter, key_function
            )
        elif algo == "Binary Search":
            self.data = self.sort_by(start, end, key, "Merge Sort", True)
            result = search_algo.jump_search(
                self.data, start, end, target, filter, key_function
            )
        elif algo == "Exponential Search":
            self.data = self.sort_by(start, end, key, "Merge Sort", True)
            result = search_algo.jump_search(
                self.data, start, end, target, filter, key_function
            )
        return result

    def search_multicolumn(self, start, end, algo, target, filter):
        result = []
        int_columns = ["Subscribers", "Likes", "Duration", "Views", "Comments"]
        string_columns = ["URL", "Channel", "Title"]
        try:
            target = int(target)
            i = 0
            while len(result) == 0 and i < 5:
                result = self.search_by(
                    start, end, algo, target, filter, int_columns[i]
                )
                i += 1
        except:
            i = 0
            while len(result) == 0 and i < 3:
                result = self.search_by(
                    start, end, algo, target, filter, string_columns[i]
                )
                i += 1
        return result
