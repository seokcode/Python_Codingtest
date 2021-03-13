//
//  베스트앨범.swift
//  Algorithm-Swift
//
//  Created by 이원석 on 2021/03/14.
//
import Foundation

func solution(_ genres:[String], _ plays:[Int]) -> [Int] {
    var playList = [String:(play: Int, music: [Int:Int])]()
    var answer = [Int]()

    for (index, value) in genres.enumerated() {
        if let genre = playList[value]?.play {
            playList[value]?.play = genre + plays[index]
            playList[value]?.music[index] = plays[index]
        } else {
            playList[value] = (play: plays[index], music: [index:plays[index]])
        }
    }

    let rank = playList.sorted(by: { $0.value.play > $1.value.play })

    rank.forEach { song in
        let songRank = song.value.music.sorted { $0.value > $01.value }

        let max = songRank.count > 1 ? 2 : 1
        for i in 0..<max {
            answer.append(songRank[i].key)
        }
    }

    return answer
}
