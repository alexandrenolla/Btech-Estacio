package com.CadastroServer.thread;

import com.CadastroServer.controller.MovimentoController;
import com.CadastroServer.controller.PessoaController;
import com.CadastroServer.model.Movimento;

import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.Socket;

public class CadastroThread extends Thread {
    private Socket clientSocket;
    private ObjectInputStream in;
    private ObjectOutputStream out;
    private MovimentoController ctrlMov;
    private PessoaController ctrlPessoa;
    public CadastroThread(Socket socket, MovimentoController ctrlMov, PessoaController ctrlPessoa) {
        this.clientSocket = socket;
        this.ctrlMov = ctrlMov;
        this.ctrlPessoa = ctrlPessoa;
    }

    @Override
    public void run() {
        try {
            out = new ObjectOutputStream(clientSocket.getOutputStream());
            in = new ObjectInputStream(clientSocket.getInputStream());

            while (true) {
                // Lógica para receber dados do cliente, criar Movimento, persistir e atualizar quantidade de produtos
                Object receivedData = in.readObject();
                if (receivedData instanceof String) {
                    String command = (String) receivedData;
                    if (command.equals("E")) {
                        // Comando para entrada de produtos
                        processEntrada();
                    } else if (command.equals("S")) {
                        // Comando para saída de produtos
                        processSaida();
                    }
                }
            }

        } catch (IOException | ClassNotFoundException e) {
            e.printStackTrace();
        } finally {
            try {
                clientSocket.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

    private void processEntrada() throws IOException, ClassNotFoundException {
        // Lógica para processar a entrada de produtos
        int pessoaId = in.readInt();
        int produtoId = in.readInt();
        int quantidade = in.readInt();
        double valorUnitario = in.readDouble();

        // Criar um objeto Movimento
        Movimento movimento = new Movimento();
        movimento.setPessoa(ctrlPessoa.findPessoa(pessoaId));
        Object ctrlProduto;
        // movimento.setProduto(((Object) ctrlProduto).findProduto(produtoId));
        movimento.setQuantidade(quantidade);
        movimento.setValorUnitario(valorUnitario);

        // Persistir o movimento
        ctrlMov.create(movimento);

        // Atualizar a quantidade de produtos
        ctrlMov.atualizarQuantidade(produtoId, quantidade);
    }

    private void processSaida() throws IOException, ClassNotFoundException {
    }
}
