package com.otacon.decks.italian;

import java.util.*;

import static com.otacon.decks.italian.ItalianCard.Type.*;

public class ItalianDeck {

    public LinkedList<ItalianCard> cards;

    public ItalianDeck() {
        cards = new LinkedList<>();
        initializeDeck();
        shuffleDeck();
    }

    public void initializeDeck() {
        cards.clear();
        addType(GOLD);
        addType(CLUBS);
        addType(SWORDS);
        addType(CUPS);
    }

    public void shuffleDeck() {
        Collections.shuffle(cards);
    }

    public ItalianCard pull() throws NoSuchElementException {
        return cards.removeFirst();
    }

    public ItalianCard pick() {
        return cards.peek();
    }

    private void addType(ItalianCard.Type t) {
        for (int i = 1; i <= 10; i++) {
            cards.add(new ItalianCard(t, ItalianCard.Value.getByNumericValue(i)));
        }
    }

    @Override
    public String toString() {
        return "ItalianDeck{" +
                "cards=" + cards + "\n" +
                "size=" + cards.size() + "\n" +
                '}';
    }
}
