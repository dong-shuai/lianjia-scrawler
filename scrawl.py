import core
import model
import settings

def get_communitylist():
	res = []
	for community in model.Community.select():
		res.append(community.title)
	return res

if __name__=="__main__":
    regionlist = settings.REGIONLIST # only pinyin support
    model.database_init() # only run on the first time
    # ByRegionlist cant not get all data because linajie only display 100 pages
    # core.GetHouseByRegionlist(regionlist)
    # core.GetRentByRegionlist(regionlist)
    
    # Init,scrapy celllist and insert database; could run only 1st time
    core.GetCommunityByRegionlist(regionlist) 
    
    # Read celllist from database
    communitylist = get_communitylist()
    
    # history sell
    core.GetSellByCommunitylist(communitylist)
    
    # on sell
    core.GetHouseByCommunitylist(communitylist)

    # Rent 
    core.GetRentByCommunitylist(communitylist)