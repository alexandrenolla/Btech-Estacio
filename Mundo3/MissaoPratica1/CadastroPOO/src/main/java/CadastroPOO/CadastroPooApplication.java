package CadastroPOO;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import CadastroPOO.model.PessoaFisica;
import CadastroPOO.model.PessoaJuridica;
import CadastroPOO.repository.PessoaFisicaRepository;
import CadastroPOO.repository.PessoaJuridicaRepository;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;

@SpringBootApplication
public class CadastroPooApplication {

    private static final Scanner scanner = new Scanner(System.in);
    private static final PessoaFisicaRepository pessoaFisicaRepository = new PessoaFisicaRepository();
    private static final PessoaJuridicaRepository pessoaJuridicaRepository = new PessoaJuridicaRepository();

    public static void main(String[] args) {
        int escolha;

        do {
            exibirMenu();
            System.out.print("Escolha uma opção: ");
            escolha = scanner.nextInt();

            switch (escolha) {
                case 1:
                    incluirPessoa();
                    break;
                case 2:
                    alterarPessoa();
                    break;
                case 3:
                    excluirPessoa();
                    break;
                case 4:
                    buscarPessoaPorId();
                    break;
                case 5:
                    exibirTodasPessoas();
                    break;
                case 6:
                    persistirDados();
                    break;
                case 7:
                    recuperarDados();
                    break;
                case 0:
                    System.out.println("Programa finalizado.");
                    break;
                default:
                    System.out.println("Opção inválida. Tente novamente.");
            }

        } while (escolha != 0);

        scanner.close();
    }

    private static void exibirMenu() {
        System.out.println("==================================");
        System.out.println("1 - Incluir Pessoa");
        System.out.println("2 - Alterar Pessoa");
        System.out.println("3 - Excluir Pessoa");
        System.out.println("4 - Buscar pelo Id");
        System.out.println("5 - Exibir Todos");
        System.out.println("6 - Persistir Dados");
        System.out.println("7 - Recuperar Dados");
        System.out.println("0 - Finalizar Programa");
        System.out.println("==================================");
    }

    private static void incluirPessoa() {
        System.out.println("F - Pessoa Fisica | J - Pessoa Juridica");
        char tipo = scanner.next().toUpperCase().charAt(0);

        System.out.println("Digite o id da pessoa:");
        int id = scanner.nextInt();
        scanner.nextLine(); // Limpa o buffer do scanner

        System.out.println("Insira os dados. . .");
        System.out.println("Nome:");
        String nome = scanner.nextLine();

        if (tipo == 'F') {
            System.out.println("CPF:");
            String cpf = scanner.next();
            System.out.println("Idade:");
            int idade = scanner.nextInt();
            PessoaFisica pessoaFisica = new PessoaFisica(id, nome, cpf, idade);
            pessoaFisicaRepository.inserir(pessoaFisica);
            System.out.println("Pessoa Física adicionada com sucesso!");
        } else if (tipo == 'J') {
            System.out.println("CNPJ:");
            String cnpj = scanner.next();
            PessoaJuridica pessoaJuridica = new PessoaJuridica(id, nome, cnpj);
            pessoaJuridicaRepository.inserir(pessoaJuridica);
            System.out.println("Pessoa Jurídica adicionada com sucesso!");
        }
    }

    private static void alterarPessoa() {
        System.out.println("Digite o id da pessoa que deseja alterar:");
        int id = scanner.nextInt();

        System.out.println("F - Pessoa Fisica | J - Pessoa Juridica");
        char tipo = scanner.next().toUpperCase().charAt(0);

        scanner.nextLine(); // Limpa o buffer do scanner

        System.out.println("Insira os novos dados. . .");
        System.out.println("Nome:");
        String nome = scanner.nextLine();

        if (tipo == 'F') {
            System.out.println("CPF:");
            String cpf = scanner.next();
            System.out.println("Idade:");
            int idade = scanner.nextInt();
            PessoaFisica pessoaFisica = new PessoaFisica(id, nome, cpf, idade);
            pessoaFisicaRepository.alterar(pessoaFisica);
            System.out.println("Pessoa Física alterada com sucesso!");
        } else if (tipo == 'J') {
            System.out.println("CNPJ:");
            String cnpj = scanner.next();
            PessoaJuridica pessoaJuridica = new PessoaJuridica(id, nome, cnpj);
            pessoaJuridicaRepository.alterar(pessoaJuridica);
            System.out.println("Pessoa Jurídica alterada com sucesso!");
        }
    }

    private static void excluirPessoa() {
        System.out.println("Digite o id da pessoa que deseja excluir:");
        int id = scanner.nextInt();

        System.out.println("F - Pessoa Fisica | J - Pessoa Juridica");
        char tipo = scanner.next().toUpperCase().charAt(0);

        if (tipo == 'F') {
            pessoaFisicaRepository.excluir(id);
            System.out.println("Pessoa Física excluída com sucesso!");
        } else if (tipo == 'J') {
            pessoaJuridicaRepository.excluir(id);
            System.out.println("Pessoa Jurídica excluída com sucesso!");
        }
    }

    private static void buscarPessoaPorId() {
        System.out.println("Digite o id da pessoa que deseja buscar:");
        int id = scanner.nextInt();

        System.out.println("F - Pessoa Fisica | J - Pessoa Juridica");
        char tipo = scanner.next().toUpperCase().charAt(0);

        if (tipo == 'F') {
            PessoaFisica pessoaFisica = pessoaFisicaRepository.obter(id);
            if (pessoaFisica != null) {
                System.out.println("Pessoa Física encontrada:");
                pessoaFisica.exibir();
            } else {
                System.out.println("Pessoa Física não encontrada.");
            }
        } else if (tipo == 'J') {
            PessoaJuridica pessoaJuridica = pessoaJuridicaRepository.obter(id);
            if (pessoaJuridica != null) {
                System.out.println("Pessoa Jurídica encontrada:");
                pessoaJuridica.exibir();
            } else {
                System.out.println("Pessoa Jurídica não encontrada.");
            }
        }
    }

    private static void exibirTodasPessoas() {
        System.out.println("F - Pessoa Fisica | J - Pessoa Juridica");
        char tipo = scanner.next().toUpperCase().charAt(0);

        if (tipo == 'F') {
            ArrayList<PessoaFisica> pessoasFisicas = pessoaFisicaRepository.obterTodos();
            if (!pessoasFisicas.isEmpty()) {
                System.out.println("Pessoas Físicas cadastradas:");
                for (PessoaFisica pessoaFisica : pessoasFisicas) {
                    pessoaFisica.exibir();
                    System.out.println("-----------");
                }
            } else {
                System.out.println("Nenhuma Pessoa Física cadastrada.");
            }
        } else if (tipo == 'J') {
            ArrayList<PessoaJuridica> pessoasJuridicas = pessoaJuridicaRepository.obterTodos();
            if (!pessoasJuridicas.isEmpty()) {
                System.out.println("Pessoas Jurídicas cadastradas:");
                for (PessoaJuridica pessoaJuridica : pessoasJuridicas) {
                    pessoaJuridica.exibir();
                    System.out.println("-----------");
                }
            } else {
                System.out.println("Nenhuma Pessoa Jurídica cadastrada.");
            }
        }
    }

    private static void persistirDados() {
        System.out.println("Digite o nome do arquivo para persistir os dados:");
        String arquivo = scanner.next();

        try {
            pessoaFisicaRepository.persistir(arquivo + "_fisicas.ser");
            pessoaJuridicaRepository.persistir(arquivo + "_juridicas.ser");
            System.out.println("Dados persistidos com sucesso!");
        } catch (IOException e) {
            System.out.println("Erro ao persistir os dados: " + e.getMessage());
        }
    }

    private static void recuperarDados() {
        System.out.println("Digite o nome do arquivo para recuperar os dados:");
        String arquivo = scanner.next();

        try {
            pessoaFisicaRepository.recuperar(arquivo + "_fisicas.ser");
            pessoaJuridicaRepository.recuperar(arquivo + "_juridicas.ser");
            System.out.println("Dados recuperados com sucesso!");
        } catch (IOException | ClassNotFoundException e) {
            System.out.println("Erro ao recuperar os dados: " + e.getMessage());
        }
    }
}
