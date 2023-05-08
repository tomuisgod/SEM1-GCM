//
//  ContentView.swift
//  Shared
//
//  Created by Tomáš Lovrant on 08/05/2023.
//

import SwiftUI

struct ContentView: View {
    @StateObject var hra = class_gm()
    
    var body: some View
    {
        let bVelkost = CGFloat(5)
        VStack(spacing: bVelkost)
        {
            ForEach(0...2, id: \.self){
                row in
                HStack(spacing: bVelkost)
                {
                    ForEach(0...2, id: \.self)
                    {
                        column in
                        
                        let cell = hra.hra[row][column]
                        
                        Text(cell.displayTile())
                            .font(.system(size: 60))
                            .foregroundColor(cell.tileColor())
                            .bold()
                            .frame(maxWidth: .infinity, maxHeight: .infinity)
                            .aspectRatio(1, contentMode: .fit)
                            .background(Color.white)
                            .onTapGesture(
                                hra.placeTile(row, column)
                            )
                    }
                }
            }
            
        }
        .background(Color.black)
        .padding()
        
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
