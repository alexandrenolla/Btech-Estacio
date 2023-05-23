export default class Livro {
    codigo: number;
    codigoEditora: number;
    titulo: string;
    resumo: string;
    autores: string[];
  
    constructor(codigo: number, codEditora: number, titulo: string, resumo: string, autores: string[]) {
      this.codigo = codigo;
      this.codigoEditora = codEditora;
      this.titulo = titulo;
      this.resumo = resumo;
      this.autores = autores;
    }
}
  