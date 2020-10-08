from main_script import get_watchlists
import sys

watchlists = get_watchlists()
print(watchlists)

def watchlist_update(): 
    print('Watchlist name to update: ')
    name = input(str)
    for watchlist in watchlists:
        if name == watchlist['name']:
            watchlist_id =  watchlist['id']
        else:
            print('No such watchlist')
            sys.exit()
    
    print('Symbol: ')
    sym = input(str)
    add_symbol(watchlist_id, sym)

update = watchlist_update()