def slope_style_score(scores):
	scores.remove(min(scores))
	scores.remove(max(scores))
	return round(sum(scores)/len(scores)-0.005,2) 
