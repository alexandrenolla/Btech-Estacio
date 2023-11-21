package com.CadastroDB;

import com.CadastroDB.dao.PessoaFisicaDAO;
import com.CadastroDB.dao.PessoaJuridicaDAO;
import com.CadastroDB.model.PessoaFisica;
import com.CadastroDB.model.PessoaJuridica;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;

import java.util.List;
import java.util.Scanner;

@SpringBootApplication
@ComponentScan(basePackages = "com.CadastroDB")
public class CadastroDbApplication {

    public static void main(String[] args) {
        SpringApplication.run(CadastroDbApplication.class, args);
    }

    @Bean
    public CommandLineRunner cadastroRunner(PessoaFisicaDAO pessoaFisicaDAO, PessoaJuridicaDAO pessoaJuridicaDAO) {
        return args -> {
            Scanner scanner = new Scanner(System.in);

            int opcao;
            do {
                System.out.println("=========================");
                System.out.println("1 - Incluir Pessoa");
                System.out.println("2 - Alterar Pessoa");
                System.out.println("3 - Excluir Pessoa");
                System.out.println("4 - Buscar pelo Id");
                System.out.println("5 - Exibir Todos");
                System.out.println("0 - Finalizar Programa");
                System.out.println("=========================");
                System.out.print("Escolha uma opção: ");
                opcao = scanner.nextInt();
                scanner.nextLine(); // Limpar o buffer do teclado

                switch (opcao) {
                    case 1:
                        // Incluir Pessoa
                        char tipoPessoaIncluir = escolherTipoPessoa(scanner);
                        if (tipoPessoaIncluir == 'F') {
                            PessoaFisica pf = new PessoaFisica();
                            System.out.println("Digite os dados da Pessoa Física:");
                            preencherDadosPessoaFisica(pf, scanner);
                            pessoaFisicaDAO.incluir(pf);
                        } else if (tipoPessoaIncluir == 'J') {
                            PessoaJuridica pj = new PessoaJuridica();
                            System.out.println("Digite os dados da Pessoa Jurídica:");
                            preencherDadosPessoaJuridica(pj, scanner);
                            pessoaJuridicaDAO.incluir(pj);
                        } else {
                            System.out.println("Opção inválida");
                        }
                        break;
                    case 2:
                        // Alterar Pessoa
                        char tipoPessoaAlterar = escolherTipoPessoa(scanner);
                        if (tipoPessoaAlterar == 'F') {
                            // Lógica para alterar Pessoa Física
                            System.out.print("Digite o ID da Pessoa Física a ser alterada: ");
                            long idAlterarPf = scanner.nextLong();
                            scanner.nextLine(); // Limpar o buffer do teclado
                            PessoaFisica pfAlterar = pessoaFisicaDAO.getPessoa(idAlterarPf);
                            if (pfAlterar != null) {
                                System.out.println("Digite os novos dados da Pessoa Física:");
                                preencherDadosPessoaFisica(pfAlterar, scanner);
                                pessoaFisicaDAO.alterar(pfAlterar);
                                System.out.println("Pessoa Física alterada com sucesso!");
                            } else {
                                System.out.println("Pessoa Física não encontrada.");
                            }
                        } else if (tipoPessoaAlterar == 'J') {
                            // Lógica para alterar Pessoa Jurídica
                            System.out.print("Digite o ID da Pessoa Jurídica a ser alterada: ");
                            long idAlterarPj = scanner.nextLong();
                            scanner.nextLine(); // Limpar o buffer do teclado
                            PessoaJuridica pjAlterar = pessoaJuridicaDAO.getPessoa(idAlterarPj);
                            if (pjAlterar != null) {
                                System.out.println("Digite os novos dados da Pessoa Jurídica:");
                                preencherDadosPessoaJuridica(pjAlterar, scanner);
                                pessoaJuridicaDAO.alterar(pjAlterar);
                                System.out.println("Pessoa Jurídica alterada com sucesso!");
                            } else {
                                System.out.println("Pessoa Jurídica não encontrada.");
                            }
                        } else {
                            System.out.println("Opção inválida");
                        }
                        break;
                    case 3:
                        // Excluir Pessoa Física ou Jurídica
                        char tipoPessoaExcluir = escolherTipoPessoa(scanner);
                        if (tipoPessoaExcluir == 'F') {
                            System.out.print("Digite o ID da Pessoa Física a ser excluída: ");
                            long idExcluirPf = scanner.nextLong();
                            scanner.nextLine(); // Limpar o buffer do teclado
                            PessoaFisica pfExcluir = pessoaFisicaDAO.getPessoa(idExcluirPf);
                            if (pfExcluir != null) {
                                pessoaFisicaDAO.excluir(idExcluirPf);
                                System.out.println("Pessoa Física excluída com sucesso!");
                            } else {
                                System.out.println("Pessoa Física não encontrada.");
                            }
                        } else if (tipoPessoaExcluir == 'J') {
                            System.out.print("Digite o ID da Pessoa Jurídica a ser excluída: ");
                            long idExcluirPj = scanner.nextLong();
                            scanner.nextLine(); // Limpar o buffer do teclado
                            PessoaJuridica pjExcluir = pessoaJuridicaDAO.getPessoa(idExcluirPj);
                            if (pjExcluir != null) {
                                pessoaJuridicaDAO.excluir(idExcluirPj);
                                System.out.println("Pessoa Jurídica excluída com sucesso!");
                            } else {
                                System.out.println("Pessoa Jurídica não encontrada.");
                            }
                        } else {
                            System.out.println("Opção inválida");
                        }
                    break;
                    case 4:
                        // Buscar Pessoa Física ou Jurídica pelo Id
                        char tipoPessoaBuscar = escolherTipoPessoa(scanner);
                        if (tipoPessoaBuscar == 'F') {
                            System.out.print("Digite o ID da Pessoa Física a ser buscada: ");
                            long idBuscarPf = scanner.nextLong();
                            scanner.nextLine(); // Limpar o buffer do teclado
                            PessoaFisica pfBuscar = pessoaFisicaDAO.getPessoa(idBuscarPf);
                            if (pfBuscar != null) {
                                System.out.println("Dados da Pessoa Física encontrada:");
                                exibirDetalhesPessoaFisica(pfBuscar);
                            } else {
                                System.out.println("Pessoa Física não encontrada.");
                            }
                        } else if (tipoPessoaBuscar == 'J') {
                            // Lógica para buscar Pessoa Jurídica
                            System.out.print("Digite o ID da Pessoa Jurídica a ser buscada: ");
                            long idBuscarPj = scanner.nextLong();
                            scanner.nextLine(); // Limpar o buffer do teclado
                            PessoaJuridica pjBuscar = pessoaJuridicaDAO.getPessoa(idBuscarPj);
                            if (pjBuscar != null) {
                                System.out.println("Dados da Pessoa Jurídica encontrada:");
                                exibirDetalhesPessoaJuridica(pjBuscar);
                            } else {
                                System.out.println("Pessoa Jurídica não encontrada.");
                            }
                        } else {
                            System.out.println("Opção inválida");
                        }
                        break;
                    case 5:
                        // Exibir Todas Pessoas (Físicas e Jurídicas)
                        List<PessoaFisica> todasPf = pessoaFisicaDAO.getPessoas();
                        List<PessoaJuridica> todasPj = pessoaJuridicaDAO.getPessoas();

                        System.out.println("Lista de Todas Pessoas Físicas:");
                        for (PessoaFisica pessoa : todasPf) {
                            exibirDetalhesPessoaFisica(pessoa);
                        }

                        System.out.println("Lista de Todas Pessoas Jurídicas:");
                        for (PessoaJuridica pessoa : todasPj) {
                            exibirDetalhesPessoaJuridica(pessoa);
                        }
                        break;
                        case 0:
                            // Finalizar Programa
                            System.out.println("Programa encerrado.");
                            break;
                        default:
                            System.out.println("Opção inválida. Tente novamente.");
                            break;
                }

            } while (opcao != 0);

            scanner.close();
        };
    }

    private char escolherTipoPessoa(Scanner scanner) {
        System.out.print("F - Pessoa Fisica | J - Pessoa Juridica: ");
        return scanner.next().charAt(0);
    }

    private void preencherDadosPessoaFisica(PessoaFisica pessoa, Scanner scanner) {
        System.out.print("Nome: ");
        pessoa.setNome(scanner.nextLine());
        System.out.print("Logradouro: ");
        pessoa.setLogradouro(scanner.nextLine());
        System.out.print("Cidade: ");
        pessoa.setCidade(scanner.nextLine());
        System.out.print("Estado: ");
        pessoa.setEstado(scanner.nextLine());
        System.out.print("Telefone: ");
        pessoa.setTelefone(scanner.nextLine());
        System.out.print("Email: ");
        pessoa.setEmail(scanner.nextLine());
        System.out.print("CPF: ");
        pessoa.setCpf(scanner.nextLine());
    }

    private void preencherDadosPessoaJuridica(PessoaJuridica pessoa, Scanner scanner) {
        System.out.print("Nome: ");
        pessoa.setNome(scanner.nextLine());
        System.out.print("Logradouro: ");
        pessoa.setLogradouro(scanner.nextLine());
        System.out.print("Cidade: ");
        pessoa.setCidade(scanner.nextLine());
        System.out.print("Estado: ");
        pessoa.setEstado(scanner.nextLine());
        System.out.print("Telefone: ");
        pessoa.setTelefone(scanner.nextLine());
        System.out.print("Email: ");
        pessoa.setEmail(scanner.nextLine());
        System.out.print("CNPJ: ");
        pessoa.setCnpj(scanner.nextLine());
    }

    private void exibirDetalhesPessoaFisica(PessoaFisica pessoa) {
        System.out.println("Id: " + pessoa.getId());
        System.out.println("Nome: " + pessoa.getNome());
        System.out.println("Logradouro: " + pessoa.getLogradouro());
        System.out.println("Cidade: " + pessoa.getCidade());
        System.out.println("Estado: " + pessoa.getEstado());
        System.out.println("Telefone: " + pessoa.getTelefone());
        System.out.println("Email: " + pessoa.getEmail());
        System.out.println("CPF: " + pessoa.getCpf());
    }
    
    private void exibirDetalhesPessoaJuridica(PessoaJuridica pessoa) {
        System.out.println("Id: " + pessoa.getId());
        System.out.println("Nome: " + pessoa.getNome());
        System.out.println("Logradouro: " + pessoa.getLogradouro());
        System.out.println("Cidade: " + pessoa.getCidade());
        System.out.println("Estado: " + pessoa.getEstado());
        System.out.println("Telefone: " + pessoa.getTelefone());
        System.out.println("Email: " + pessoa.getEmail());
        System.out.println("CNPJ: " + pessoa.getCnpj());
    }
}
