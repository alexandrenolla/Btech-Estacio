package com.CadastroClient.thread;

import java.io.ObjectInputStream;
import javax.swing.JTextArea;
import javax.swing.SwingUtilities;

public class ThreadClient extends Thread {

    private ObjectInputStream entrada;
    private JTextArea textArea;

    public ThreadClient(ObjectInputStream entrada, JTextArea textArea) {
        this.entrada = entrada;
        this.textArea = textArea;
    }

    @Override
    public void run() {
        try {
            while (true) {
                // Receber dados do servidor via readObject
                Object dados = entrada.readObject();

                // Adicionar dados ao JTextArea usando invokeLater
                SwingUtilities.invokeLater(() -> {
                    textArea.append(dados.toString() + "\n");
                });
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
