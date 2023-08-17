import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;

public class PacmanGame extends JPanel implements ActionListener {

    public PacmanGame() {
        // Constructor: Initialize variables, load images, and set up the game loop

        Timer timer = new Timer(40, this);
        timer.start();

        addKeyListener(new TAdapter());
        setFocusable(true);

        initGame();
    }



    @Override
    public void actionPerformed(ActionEvent e) {
       
        repaint();
    }
}
