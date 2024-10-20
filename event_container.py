
import logging
from typing import Callable
import pygame as pg

class Event():
    def __init__(self, uid: int, *args):
        self.__event_id = uid
        self.__delegats: list[Callable] = []
    
    @property
    def uid(self):
        return self.__event_id

    @property
    def delegats(self):
        return self.__delegats
    
    def subscribe(self, func:Callable):
        self.__delegats.append(func)

    def unsubscribe(self, func:Callable):
        self.__delegats.remove(func)

    def invoke(self, **kwargs):
        for delegate in self.__delegats:
            delegate(**kwargs)
        



class EventService():
    def __init__(self):
        self.__events: dict[int, Event] = dict()
        self.__system_events: dict[int, Event] = {pg.QUIT: Event(pg.QUIT),
                                                  pg.MOUSEBUTTONDOWN: Event(pg.MOUSEBUTTONDOWN),
                                                  pg.MOUSEMOTION: Event(pg.MOUSEMOTION)}

    def register_event(self, uid:int, event:Event = None):
        if uid in self.__system_events and event:
            for f in event.delegats:
                self.__system_events[uid].subscribe(f)
                return

        if not(uid in self.__events):
            self.__events[uid] = event if event else Event(uid)
            logging.info(f"[Event Service]: register event {uid}")

    def sytem_handlle(self, uid:int, func:Callable):
        if uid in self.__system_events:
            self.__system_events[uid].subscribe(func)
            logging.info(f"[Event Service]: subscribed system event {uid}")

    def subscribe(self, uid:int, func:Callable):
        if uid in self.__events:
            self.__events[uid].subscribe(func)
            logging.info(f"[Event Service]: subscribed event {uid}")

    def unsubscribe(self,uid:int, func:Callable):
        if uid in self.__events:
            self.__events[uid].unsubscribe(func)
            logging.info(f"[Event Service]: unsubscribed event {uid}")
                
    def procces_system_events(self):
        current_system_events = pg.event.get()
        for e in self.__system_events:
            for s_e in current_system_events:
                if e == s_e.type:
                    self.__system_events[e].invoke(**s_e.__dict__)