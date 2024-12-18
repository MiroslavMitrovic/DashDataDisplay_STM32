PULSONIX_LIBRARY_ASCII "SamacSys ECAD Model"
//660767/1372705/2.50/10/2/Connector

(asciiHeader
	(fileUnits MM)
)
(library Library_1
	(padStyleDef "r279_74"
		(holeDiam 0)
		(padShape (layerNumRef 1) (padShapeType Rect)  (shapeWidth 0.74) (shapeHeight 2.79))
		(padShape (layerNumRef 16) (padShapeType Ellipse)  (shapeWidth 0) (shapeHeight 0))
	)
	(padStyleDef "c51_h102"
		(holeDiam 1.02)
		(padShape (layerNumRef 1) (padShapeType Ellipse)  (shapeWidth 0.51) (shapeHeight 0.51))
		(padShape (layerNumRef 16) (padShapeType Ellipse)  (shapeWidth 0.51) (shapeHeight 0.51))
	)
	(textStyleDef "Normal"
		(font
			(fontType Stroke)
			(fontFace "Helvetica")
			(fontHeight 1.27)
			(strokeWidth 0.127)
		)
	)
	(patternDef "FTSH-105-XX-YYY-DV-A" (originalName "FTSH-105-XX-YYY-DV-A")
		(multiLayer
			(pad (padNum 1) (padStyleRef r279_74) (pt -2.54, -2.035) (rotation 0))
			(pad (padNum 2) (padStyleRef r279_74) (pt -2.54, 2.035) (rotation 0))
			(pad (padNum 3) (padStyleRef r279_74) (pt -1.27, -2.035) (rotation 0))
			(pad (padNum 4) (padStyleRef r279_74) (pt -1.27, 2.035) (rotation 0))
			(pad (padNum 5) (padStyleRef r279_74) (pt 0, -2.035) (rotation 0))
			(pad (padNum 6) (padStyleRef r279_74) (pt 0, 2.035) (rotation 0))
			(pad (padNum 7) (padStyleRef r279_74) (pt 1.27, -2.035) (rotation 0))
			(pad (padNum 8) (padStyleRef r279_74) (pt 1.27, 2.035) (rotation 0))
			(pad (padNum 9) (padStyleRef r279_74) (pt 2.54, -2.035) (rotation 0))
			(pad (padNum 10) (padStyleRef r279_74) (pt 2.54, 2.035) (rotation 0))
			(pad (padNum 11) (padStyleRef c51_h102) (pt -1.905, 0) (rotation 90))
			(pad (padNum 12) (padStyleRef c51_h102) (pt 1.905, 0) (rotation 90))
		)
		(layerContents (layerNumRef 18)
			(attr "RefDes" "RefDes" (pt 0, 0) (textStyleRef "Normal") (isVisible True))
		)
		(layerContents (layerNumRef 28)
			(line (pt -3.175 1.715) (pt 3.175 1.715) (width 0.025))
		)
		(layerContents (layerNumRef 28)
			(line (pt 3.175 1.715) (pt 3.175 -1.715) (width 0.025))
		)
		(layerContents (layerNumRef 28)
			(line (pt 3.175 -1.715) (pt -3.175 -1.715) (width 0.025))
		)
		(layerContents (layerNumRef 28)
			(line (pt -3.175 -1.715) (pt -3.175 1.715) (width 0.025))
		)
		(layerContents (layerNumRef 18)
			(line (pt 3.175 1.715) (pt 3.175 -1.715) (width 0.1))
		)
		(layerContents (layerNumRef 18)
			(line (pt -3.175 -1.715) (pt -3.175 1.715) (width 0.1))
		)
		(layerContents (layerNumRef 18)
			(arc (pt -2.59, -3.785) (radius 0.05) (startAngle 0.0) (sweepAngle 0.0) (width 0.2))
		)
		(layerContents (layerNumRef 18)
			(arc (pt -2.59, -3.785) (radius 0.05) (startAngle 180.0) (sweepAngle 180.0) (width 0.2))
		)
		(layerContents (layerNumRef Courtyard_Top)
			(line (pt -4.375 4.43) (pt 4.375 4.43) (width 0.05))
		)
		(layerContents (layerNumRef Courtyard_Top)
			(line (pt 4.375 4.43) (pt 4.375 -4.885) (width 0.05))
		)
		(layerContents (layerNumRef Courtyard_Top)
			(line (pt 4.375 -4.885) (pt -4.375 -4.885) (width 0.05))
		)
		(layerContents (layerNumRef Courtyard_Top)
			(line (pt -4.375 -4.885) (pt -4.375 4.43) (width 0.05))
		)
	)
	(symbolDef "FTSH-105-01-L-DV-A" (originalName "FTSH-105-01-L-DV-A")

		(pin (pinNum 1) (pt 0 mils 0 mils) (rotation 0) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 230 mils -25 mils) (rotation 0]) (justify "Left") (textStyleRef "Normal"))
		))
		(pin (pinNum 2) (pt 900 mils 0 mils) (rotation 180) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 670 mils -25 mils) (rotation 0]) (justify "Right") (textStyleRef "Normal"))
		))
		(pin (pinNum 3) (pt 0 mils -100 mils) (rotation 0) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 230 mils -125 mils) (rotation 0]) (justify "Left") (textStyleRef "Normal"))
		))
		(pin (pinNum 4) (pt 900 mils -100 mils) (rotation 180) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 670 mils -125 mils) (rotation 0]) (justify "Right") (textStyleRef "Normal"))
		))
		(pin (pinNum 5) (pt 0 mils -200 mils) (rotation 0) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 230 mils -225 mils) (rotation 0]) (justify "Left") (textStyleRef "Normal"))
		))
		(pin (pinNum 6) (pt 900 mils -200 mils) (rotation 180) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 670 mils -225 mils) (rotation 0]) (justify "Right") (textStyleRef "Normal"))
		))
		(pin (pinNum 7) (pt 0 mils -300 mils) (rotation 0) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 230 mils -325 mils) (rotation 0]) (justify "Left") (textStyleRef "Normal"))
		))
		(pin (pinNum 8) (pt 900 mils -300 mils) (rotation 180) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 670 mils -325 mils) (rotation 0]) (justify "Right") (textStyleRef "Normal"))
		))
		(pin (pinNum 9) (pt 0 mils -400 mils) (rotation 0) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 230 mils -425 mils) (rotation 0]) (justify "Left") (textStyleRef "Normal"))
		))
		(pin (pinNum 10) (pt 900 mils -400 mils) (rotation 180) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 670 mils -425 mils) (rotation 0]) (justify "Right") (textStyleRef "Normal"))
		))
		(line (pt 200 mils 100 mils) (pt 700 mils 100 mils) (width 6 mils))
		(line (pt 700 mils 100 mils) (pt 700 mils -500 mils) (width 6 mils))
		(line (pt 700 mils -500 mils) (pt 200 mils -500 mils) (width 6 mils))
		(line (pt 200 mils -500 mils) (pt 200 mils 100 mils) (width 6 mils))
		(attr "RefDes" "RefDes" (pt 750 mils 300 mils) (justify Left) (isVisible True) (textStyleRef "Normal"))
		(attr "Type" "Type" (pt 750 mils 200 mils) (justify Left) (isVisible True) (textStyleRef "Normal"))

	)
	(compDef "FTSH-105-01-L-DV-A" (originalName "FTSH-105-01-L-DV-A") (compHeader (numPins 10) (numParts 1) (refDesPrefix J)
		)
		(compPin "1" (pinName "1") (partNum 1) (symPinNum 1) (gateEq 0) (pinEq 0) (pinType Unknown))
		(compPin "2" (pinName "2") (partNum 1) (symPinNum 2) (gateEq 0) (pinEq 0) (pinType Unknown))
		(compPin "3" (pinName "3") (partNum 1) (symPinNum 3) (gateEq 0) (pinEq 0) (pinType Unknown))
		(compPin "4" (pinName "4") (partNum 1) (symPinNum 4) (gateEq 0) (pinEq 0) (pinType Unknown))
		(compPin "5" (pinName "5") (partNum 1) (symPinNum 5) (gateEq 0) (pinEq 0) (pinType Unknown))
		(compPin "6" (pinName "6") (partNum 1) (symPinNum 6) (gateEq 0) (pinEq 0) (pinType Unknown))
		(compPin "7" (pinName "7") (partNum 1) (symPinNum 7) (gateEq 0) (pinEq 0) (pinType Unknown))
		(compPin "8" (pinName "8") (partNum 1) (symPinNum 8) (gateEq 0) (pinEq 0) (pinType Unknown))
		(compPin "9" (pinName "9") (partNum 1) (symPinNum 9) (gateEq 0) (pinEq 0) (pinType Unknown))
		(compPin "10" (pinName "10") (partNum 1) (symPinNum 10) (gateEq 0) (pinEq 0) (pinType Unknown))
		(attachedSymbol (partNum 1) (altType Normal) (symbolName "FTSH-105-01-L-DV-A"))
		(attachedPattern (patternNum 1) (patternName "FTSH-105-XX-YYY-DV-A")
			(numPads 10)
			(padPinMap
				(padNum 1) (compPinRef "1")
				(padNum 2) (compPinRef "2")
				(padNum 3) (compPinRef "3")
				(padNum 4) (compPinRef "4")
				(padNum 5) (compPinRef "5")
				(padNum 6) (compPinRef "6")
				(padNum 7) (compPinRef "7")
				(padNum 8) (compPinRef "8")
				(padNum 9) (compPinRef "9")
				(padNum 10) (compPinRef "10")
			)
		)
		(attr "Mouser Part Number" "200-FTSH10501LDVA")
		(attr "Mouser Price/Stock" "https://www.mouser.co.uk/ProductDetail/Samtec/FTSH-105-01-L-DV-A?qs=vqM95g%252BRBeykLJELFbssPw%3D%3D")
		(attr "Manufacturer_Name" "SAMTEC")
		(attr "Manufacturer_Part_Number" "FTSH-105-01-L-DV-A")
		(attr "Description" "10 Position, High Reliability Header Strips, 0.050&quot; pitch")
		(attr "<Hyperlink>" "http://suddendocs.samtec.com/prints/ftsh-1xx-xx-xxx-dv-xxx-xxx-mkt.pdf")
	)

)
