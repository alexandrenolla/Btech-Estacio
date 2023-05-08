// Function Swap -------------------------------------------------------------------------------------------------------------------
const swap = (vetor, pos1, pos2) => {
  // Valor da posição 1
  const valorPos1 = vetor[pos1]
  // Atribuindo o valor da posição 2 para a posição 1
  vetor[pos1] = vetor[pos2]
  // Atribuindo o valor salvo da posição 1 para a posição 2
  vetor[pos2] = valorPos1
  return vetor
}
const vetorSwap = [1, 2, 3, 4, 5];
swap(vetorSwap, 1, 3)
console.log(`Função Swap: ${vetorSwap}`)

// Function Shuffle ----------------------------------------------------------------------------------------------------------------
const shuffle = (vetor, numTrocas) => {
  for (let i = 0; i < numTrocas; i++) {
    // Escolhe dois índices aleatórios
    const index1 = Math.floor(Math.random() * vetor.length);
    const index2 = Math.floor(Math.random() * vetor.length);
    // Troca os elementos nos índices escolhidos
    [vetor[index1], vetor[index2]] = [vetor[index2], vetor[index1]];
  }
  return vetor
}
const vetorShuffle = [1, 2, 3, 4, 5];
shuffle(vetorShuffle, 2)
console.log(`Função Shuffle: ${vetorShuffle}`);

// Function Bubble Sort ------------------------------------------------------------------------------------------------------------
const bubbleSort = (vetor) => {
  const len = vetor.length;
  let trocou;
  do {
    trocou = false;
    for (let i = 0; i < len - 1; i++) {
      if (vetor[i] > vetor[i + 1]) {
        [vetor[i], vetor[i + 1]] = [vetor[i + 1], vetor[i]];
        trocou = true;
      }
    }
  } while (trocou);
  return vetor;
}
const vetorBubbleSort = [9, 0, 3, 1, 2, 7, 8, 6, 5, 4];
bubbleSort(vetorBubbleSort)
console.log(`Função Bubble Sort: ${vetorBubbleSort}`)

// Function Selection Sort ---------------------------------------------------------------------------------------------------------
const selectionSort = (vetor) => {
  for (let i = 0; i < vetor.length - 1; i++) {
    let minIndex = i;
    for (let j = i + 1; j < vetor.length; j++) {
      if (vetor[j] < vetor[minIndex]) {
        minIndex = j;
      }
    }
    // Troca os valores das posições i e minIndex, se necessário
    if (i !== minIndex) {
      let temp = vetor[i];
      vetor[i] = vetor[minIndex];
      vetor[minIndex] = temp;
    }
  }
  return vetor;
}
const vetorSelectionSort = [9, 0, 3, 1, 2, 7, 8, 6, 5, 4];
selectionSort(vetorSelectionSort)
console.log(`Função Selection Sort: ${vetorSelectionSort}`)

// Function Quick Sort e Particionamento -------------------------------------------------------------------------------------------
const quickSort = (vetor, inicio = 0, fim = vetor.length - 1) => {
  if (inicio < fim) {
    let pivo = partition(vetor, inicio, fim);
    quickSort(vetor, inicio, pivo - 1);
    quickSort(vetor, pivo + 1, fim);
  }
  return vetor;
}

function partition(vetor, inicio, fim) {
  let pivo = vetor[fim];
  let i = inicio - 1;
  for (let j = inicio; j < fim; j++) {
    if (vetor[j] <= pivo) {
      i++;
      let temp = vetor[i];
      vetor[i] = vetor[j];
      vetor[j] = temp;
    }
  }
  let temp = vetor[i + 1];
  vetor[i + 1] = vetor[fim];
  vetor[fim] = temp;
  return i + 1;
}

const vetorQuickSort = [9, 0, 3, 1, 2, 7, 8, 6, 5, 4];
selectionSort(vetorQuickSort)
console.log(`Função Quick Sort: ${vetorQuickSort}`)