import { Injectable } from '@angular/core';
import { Editora } from './editora';

@Injectable({
  providedIn: 'root'
})
export class ControleEditoraService {

  editoras: Array<Editora> = [
    {
      codEditora: 1,
      nome: "Editora A"
    },
    {
      codEditora: 2,
      nome: "Editora B"
    },
    {
      codEditora: 3,
      nome: "Editora C"
    }
  ];

  constructor() { }

  getNomeEditora(codEditora: number): string {
    const editora = this.editoras.filter(editora => editora.codEditora === codEditora);
    return editora.length > 0 ? editora[0].nome : '';
  }

  getEditoras(): Array<Editora> {
    return this.editoras;
  }
}