// Implementacja metody map dla tablic z wykorzystaniem generyczności
function customMap<T, U>(arr: T[], callback: (element: T, index: number, array: T[]) => U): U[] {
    const mappedArray: U[] = [];
    for (let i = 0; i < arr.length; i++) {
      const result = callback(arr[i], i, arr);
      mappedArray.push(result);
    }
    return mappedArray;
  }

  function square(num : number){
    return num * num;
  }
  function smaller_than_ten(num : number) :boolean{
    return num < 10;
  }



  let table : number[] = [1,2,3,4,5,6];

  // Implementacja metody map dla tablic z wykorzystaniem generyczności

  // Implementacja metody forEach dla tablic z wykorzystaniem generyczności
  function customForEach<T>(arr: T[], callback: (element: T, index: number, array: T[]) => void): void {
    for (let i = 0; i < arr.length; i++) {
      callback(arr[i], i, arr);
    }
  }
  
  // Implementacja metody filter dla tablic z wykorzystaniem generyczności
  function customFilter<T>(arr: T[], callback: (element: T, index: number, array: T[]) => boolean): T[] {
    const filteredArray: T[] = [];
    for (let i = 0; i < arr.length; i++) {
      if (callback(arr[i], i, arr)) {
        filteredArray.push(arr[i]);
      }
    }
    return filteredArray;
  }
  console.log(customMap(table,square))
  console.log(customFilter(table,smaller_than_ten))