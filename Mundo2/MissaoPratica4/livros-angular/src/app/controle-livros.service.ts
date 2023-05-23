import { Injectable } from '@angular/core';
import { Livro } from './livro';

@Injectable({
  providedIn: 'root'
})
export class ControleLivrosService {

  livros: Array<Livro> = [
    {
      codigo: 1,
      codEditora: 1,
      titulo: "Livro A",
      resumo: "Resumo do Livro A. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris sed luctus nulla. Donec mollis, velit id ultricies commodo, quam nulla lobortis tortor, ac faucibus eros ex non sapien.",
      autores: ["João Euclides", " Maria da Rosa"]
    },
    {
      codigo: 2,
      codEditora: 2,
      titulo: "Livro B",
      resumo: "Resumo do Livro B. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris sed luctus nulla. Donec mollis, velit id ultricies commodo, quam nulla lobortis tortor, ac faucibus eros ex non sapien.",
      autores: ["Clementina leidiane", "Artur Vieira"]
    },
    {
      codigo: 3,
      codEditora: 3,
      titulo: "Livro C",
      resumo: "Resumo do Livro C. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris sed luctus nulla. Donec mollis, velit id ultricies commodo, quam nulla lobortis tortor, ac faucibus eros ex non sapien.",
      autores: ["Valdir Vulgado", "Karina Karão"]
    },
  ];

  constructor() { }

  obterLivros(): Array<Livro> {
    return this.livros;
  }

  incluir(livro: Livro): void {
    const codigoMax = this.livros.reduce((max, livro) => {
      return livro.codigo > max ? livro.codigo : max;
    }, 0);
    livro.codigo = codigoMax + 1;
    this.livros.push(livro);
  }

  excluir(codigo: number): void {
    const index = this.livros.findIndex(livro => livro.codigo === codigo);
    if (index !== -1) {
      this.livros.splice(index, 1);
    }
  }
}