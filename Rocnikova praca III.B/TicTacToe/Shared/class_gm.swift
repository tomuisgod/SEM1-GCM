//
//  class_gm.swift
//  TicTacToe
//
//  Created by Tomáš Lovrant on 08/05/2023.
//

import Foundation
import SwiftUI

class class_gm: ObservableObject
{
    @Published var h_doska = [[Cell]]()
    
    init()
    {
        restart()
    }
    func placeTile(_ row:Int,_ column:Int)
    {
        if(h_doska[row][column].tile != Tile.prazdne)
        {
                return
        }
            
    }
    func restart()
    {
        var novaHra = [[Cell]]()
        for _ in 0...2
        {
            var r = [Cell]()
            for _ in 0...2
            {
                r.append(Cell(kk: Tile.prazdne))
                
            }
            novaHra.append(r)
        }
        h_doska = novaHra
    }
}
