# DB_booking_tracker


## Story

I am traveling frequently with Deutsche Bahn trains and seem to have the bad luck to always travel with overbooked trains. I started wondering whether I actually have bad luck or if Deutsche Bahn has certain trains structuraly overbooked. 

## Tool

The tool is going to be build from three parts, the scraper, the sheduler and the organiser. The scraper opens the website www.bahn.de, navigates to the connection and scrapes down planned time, actual time and utalisation of the next train. The Sheduler will most probably interact with the DB-Shedule API and figure our when trains are supposed to run and shedule the scraper to run shortly before planned departure time. The organiser will just write the scraped date somewhere, most likely into some sort of SQL Database.
