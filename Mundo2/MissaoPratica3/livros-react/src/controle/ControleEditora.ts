import { Editora } from '../modelo/Editora';

const editoras: Editora[] = [
    new Editora(1, "Editora 1"),
    new Editora(2, "Editora 2"),
    new Editora(3, "Editora 3")
  ];
  
export default class ControleEditora {
  public static getEditoras(): Editora[] {
    return editoras;
    }

  public static getNomeEditora(codEditora: number): string {
    const editora = editoras.filter(e => e.codigoEditora === codEditora)[0];
    return editora ? editora.nome : '';
  }
}

