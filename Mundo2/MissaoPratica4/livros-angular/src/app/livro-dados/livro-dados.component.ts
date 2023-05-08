import { Component } from '@angular/core';
import { OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ControleLivrosService } from '../controle-livros.service';
import { ControleEditoraService } from '../controle-editora.service';
import { Livro } from '../livro';
import { Editora } from '../editora';

@Component({
  selector: 'app-livro-dados',
  templateUrl: './livro-dados.component.html',
  styleUrls: ['./livro-dados.component.css']
})

export class LivroDadosComponent implements OnInit {
  livro: Livro = new Livro(0, 0, '', '', []);
  autoresForm: string = '';
  editoras: Array<Editora> = [];

  constructor(private servEditora: ControleEditoraService,
              private servLivros: ControleLivrosService,
              private router: Router) { }

  ngOnInit(): void {
    this.editoras = this.servEditora.getEditoras();
  }

  obterNome(codEditora: number): string {
    const editora = this.editoras.find(e => e.codEditora === codEditora);
    return editora ? editora.nome : '';
  }

  incluir = () => {
    this.livro.autores = this.autoresForm.split('\n').map(autor => autor.trim());
    this.servLivros.incluir(this.livro);
    this.router.navigateByUrl('/lista');

  }
 
}


