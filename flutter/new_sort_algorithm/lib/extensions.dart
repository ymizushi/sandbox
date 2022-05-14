extension Sortable on List<int> {
  Iterable<List<int>> nsort() sync* {
    List<int> copiedList = [...this];
    for (var i = 0; i < copiedList.length; i++) {
      for (var j = 0; j < copiedList.length; j++) {
        if (copiedList[i] < copiedList[j]) {
          var temp = copiedList[i];
          copiedList[i] = copiedList[j];
          copiedList[j] = temp;
          yield copiedList;
        }
      }
    }
  }
}
