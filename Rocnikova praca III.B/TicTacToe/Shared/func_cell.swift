//
//  func_cell.swift
//  TicTacToe
//
//  Created by Tomáš Lovrant on 08/05/2023.
//

import Foundation
import SwiftUI

struct Cell {
    var kk: Tile
    func displayTile() -> String
    {
        switch(kk)
        {
        case Tile.kruh:
            return "O"
        case Tile.krizik:
            return "X"
        default:
            return ""
        }
    }
    
    func kkColor() -> Color
    {
        switch(kk)
        {
        case Tile.kruh:
            return Color.blue
        case Tile.krizik:
            return Color.red
        default:
            return Color.black
        }
    }
}

enum Tile{
    case kruh
    case krizik
    case prazdne
    
}
