package com.CadastroClient.ui;

import javax.swing.JDialog;
import javax.swing.JTextArea;

public class SaidaFrame extends JDialog {

    public JTextArea texto;

    public SaidaFrame() {
        this.setTitle("Saída de Mensagens");
        this.setSize(400, 300);
        this.setModal(false);

        texto = new JTextArea();
        this.add(texto);
    }
}
