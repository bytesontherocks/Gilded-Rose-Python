class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def _update_sell_in(self, item):
        if item.name != "Sulfuras, Hand of Ragnaros":
            item.sell_in = item.sell_in - 1
        
    def update_quality(self):
        for item in self.items:
            self._update_sell_in(item)

            if item.name == "Aged Brie" or item.name == "Backstage passes to a TAFKAL80ETC concert":
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 10:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 5:
                            if item.quality < 50:
                                item.quality = item.quality + 1
            else:
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.quality = item.quality - 1
        
            if item.sell_in < 0:
                if item.name == "Aged Brie":
                    if item.quality < 50:
                        item.quality = item.quality + 1
                else:
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        item.quality = 0                        
                    else:
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality = item.quality - 1
                       
