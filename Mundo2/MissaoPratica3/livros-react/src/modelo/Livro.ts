export default class Livro {
    codigo: number;
    codigoEditora: number;
    titulo: string;
    resumo: string;
    autores: string[];
  
    constructor(codigo: number, codigoEditora: number, titulo: string, resumo: string, autores: string[]) {
      this.codigo = codigo;
      this.codigoEditora = codigoEditora;
      this.titulo = titulo;
      this.resumo = resumo;
      this.autores = autores;
    }
}
  