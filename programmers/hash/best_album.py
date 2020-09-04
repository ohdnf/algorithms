def my_solution(genres, plays):
    sorted_by_genres = dict()
    for i in range(len(genres)):
        if sorted_by_genres.get(genres[i]) == None:
            sorted_by_genres[genres[i]] = {'total_plays': plays[i], 'songs': {i: plays[i]}}
        else:
            curr_genre = sorted_by_genres.get(genres[i])
            curr_genre['total_plays'] += plays[i]
            curr_genre['songs'].update({i: plays[i]})
            sorted_by_genres[genres[i]] = curr_genre
    best_album = list()
    for item in list(sorted([stats for stats in sorted_by_genres.values()], key=lambda s: -s['total_plays'])):
        best_songs = sorted(item['songs'].items(), key=lambda song: -song[1])[:2]
        for idx, plays in best_songs:
            best_album.append(idx)
    return best_album


def best_solution(genres, plays):   # 좋아요 15
    answer = []
    d = {e:[] for e in set(genres)}
    for e in zip(genres, plays, range(len(plays))):
        d[e[0]].append([e[1] , e[2]])
    genreSort =sorted(list(d.keys()), key= lambda x: sum( map(lambda y: y[0],d[x])), reverse = True)
    for g in genreSort:
        temp = [e[1] for e in sorted(d[g],key= lambda x: (x[0], -x[1]), reverse = True)]
        answer += temp[:min(len(temp),2)]
    return answer


def pythonic_solution(genres, plays):   # 좋아요 10
    answer = []
    dic = {}
    album_list = []
    for i in range(len(genres)):
        dic[genres[i]] = dic.get(genres[i], 0) + plays[i]
        album_list.append(album(genres[i], plays[i], i))

    dic = sorted(dic.items(), key=lambda dic:dic[1], reverse=True)
    album_list = sorted(album_list, reverse=True)



    while len(dic) > 0:
        play_genre = dic.pop(0)
        print(play_genre)
        cnt = 0
        for ab in album_list:
            if play_genre[0] == ab.genre:
                answer.append(ab.track)
                cnt += 1
            if cnt == 2:
                break

    return answer


class album:
    def __init__(self, genre, play, track):
        self.genre = genre
        self.play = play
        self.track = track

    def __lt__(self, other):
        return self.play < other.play
    def __le__(self, other):
        return self.play <= other.play
    def __gt__(self, other):
        return self.play > other.play
    def __ge__(self, other):
        return self.play >= other.play
    def __eq__(self, other):
        return self.play == other.play
    def __ne__(self, other):
        return self.play != other.play


if __name__ == '__main__':
    g = ["classic", "pop", "classic", "classic", "pop"]
    p = [500, 600, 150, 800, 2500]
    ms = my_solution(g, p)
    # print(ms)
    ps = pythonic_solution(g, p)
    print(ps)