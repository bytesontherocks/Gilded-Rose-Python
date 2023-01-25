class GildedRose(object):
    MAX_QUALITY = 50
    MIN_QUALITY = 0

    def __init__(self, items):
        self.items = items

    def _update_sell_in(self, item):
        if item.name != "Sulfuras, Hand of Ragnaros":
            item.sell_in = item.sell_in - 1
    
    def _decrease_quality(self, item):
        if item.quality > GildedRose.MIN_QUALITY:
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.quality = item.quality - 1
        
    def update_quality(self):
        for item in self.items:
            self._update_sell_in(item)

            if item.name == "Aged Brie" or item.name == "Backstage passes to a TAFKAL80ETC concert":
                if item.quality < GildedRose.MAX_QUALITY:
                    item.quality = item.quality + 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 10:
                            if item.quality < GildedRose.MAX_QUALITY:
                                item.quality = item.quality + 1
                        if item.sell_in < 5:
                            if item.quality < GildedRose.MAX_QUALITY:
                                item.quality = item.quality + 1
            else:
                self._decrease_quality(item)
        
            if item.sell_in < GildedRose.MIN_QUALITY:
                if item.name == "Aged Brie":
                    if item.quality < GildedRose.MAX_QUALITY:
                        item.quality = item.quality + 1
                else:
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        item.quality = GildedRose.MIN_QUALITY                        
                    else:
                        self._decrease_quality(item)
                       
