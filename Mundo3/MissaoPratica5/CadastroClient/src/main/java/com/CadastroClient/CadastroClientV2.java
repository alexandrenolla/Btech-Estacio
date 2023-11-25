package com.CadastroClient;

import org.springframework.web.client.RestTemplate;

import java.util.Scanner;

public class CadastroClientV2 {
    private static final String SERVER_BASE_URL = "http://localhost:8080"; // Altere conforme necessário
    private static final String SERVER_ENDPOINT = SERVER_BASE_URL + "/api/cadastro";

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("Escolha uma opção: ");
            System.out.println("1. Listar");
            System.out.println("2. Entrada");
            System.out.println("3. Saída");
            System.out.println("0. Sair");

            int choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    listar();
                    break;
                case 2:
                    entrada();
                    break;
                case 3:
                    saida();
                    break;
                case 0:
                    System.exit(0);
                default:
                    System.out.println("Opção inválida. Tente novamente.");
            }
        }
    }

    private static void listar() {
        // Lógica para listar dados do servidor
        RestTemplate restTemplate = new RestTemplate();
        String result = restTemplate.getForObject(SERVER_ENDPOINT + "/listar", String.class);
        System.out.println(result);
    }

    private static void entrada() {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Informe o ID da pessoa: ");
        int pessoaId = scanner.nextInt();

        System.out.println("Informe o ID do produto: ");
        int produtoId = scanner.nextInt();

        System.out.println("Informe a quantidade: ");
        int quantidade = scanner.nextInt();

        System.out.println("Informe o valor unitário: ");
        double valorUnitario = scanner.nextDouble();

        // Criar um objeto para enviar ao servidor
        // Objeto exemplo (precisa ajustar conforme sua implementação)
        // MovimentoRequest movimentoRequest = new MovimentoRequest(pessoaId, produtoId, quantidade, valorUnitario);

        RestTemplate restTemplate = new RestTemplate();
        // restTemplate.postForObject(SERVER_ENDPOINT + "/entrada", movimentoRequest, String.class);

        System.out.println("Entrada registrada com sucesso.");
    }

    private static void saida() {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Informe o ID da pessoa: ");
        int pessoaId = scanner.nextInt();

        System.out.println("Informe o ID do produto: ");
        int produtoId = scanner.nextInt();

        System.out.println("Informe a quantidade: ");
        int quantidade = scanner.nextInt();

        System.out.println("Informe o valor unitário: ");
        double valorUnitario = scanner.nextDouble();

        // Criar um objeto para enviar ao servidor
        // MovimentoRequest movimentoRequest = new MovimentoRequest(pessoaId, produtoId, quantidade, valorUnitario);

        RestTemplate restTemplate = new RestTemplate();
        // restTemplate.postForObject(SERVER_ENDPOINT + "/saida", movimentoRequest, String.class);

        System.out.println("Saída registrada com sucesso.");
    }
}
