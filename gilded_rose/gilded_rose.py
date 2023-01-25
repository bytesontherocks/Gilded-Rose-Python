class GildedRose(object):
    MAX_QUALITY = 50
    MIN_QUALITY = 0

    def __init__(self, items):
        self.items = items

    def _update_sell_in(self, item):
        item.sell_in = item.sell_in - 1
    
    def _decrease_quality(self, item):        
        if item.quality > GildedRose.MIN_QUALITY:            
            item.quality = item.quality - 1
    
    def _increase_quality(self, item):
        if item.quality < GildedRose.MAX_QUALITY:
            item.quality = item.quality + 1
        
    def update_quality(self):
        for item in self.items:
            if item.name != "Sulfuras, Hand of Ragnaros":
                self._update_sell_in(item)

            if item.name == "Aged Brie":
                self._increase_quality(item)    
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                self._increase_quality(item)               
                if item.sell_in < 10:
                    self._increase_quality(item)
                if item.sell_in < 5:
                    self._increase_quality(item)                            
            else:
                if item.name != "Sulfuras, Hand of Ragnaros":
                    self._decrease_quality(item)
        
            if item.sell_in < 0:
                if item.name == "Aged Brie":
                    self._increase_quality(item)
                else:
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        item.quality = GildedRose.MIN_QUALITY                        
                    else:
                        if item.name != "Sulfuras, Hand of Ragnaros":
                            self._decrease_quality(item)
                       
