TEMP=`getopt -o r:t:b:u: --long rx:,tx:,baudrate:,url: -n 'test.sh' -- "$@"`
eval set -- "$TEMP"

while true ; do
    case "$1" in
        -r|--rx)
            case "$2" in
                *) RX=$2 ; shift 2 ;;
            esac ;;
        -t|--tx) 
        case "$2" in
                *) TX=$2 ; shift 2 ;;
            esac ;;
        -b|--baudrate)
            case "$2" in
                "") shift 2 ;;
                *) BAUDRATE=$2 ; shift 2 ;;
            esac ;;
        -u|--url)
            case "$2" in
                "") shift 2 ;;
                *) URL=$2 ; shift 2 ;;
            esac ;;
        --) shift ; break ;;
        *) echo "usage : ./downloadAndPrint.sh --rx 20 --tx 34 --baudrate 19200 --url http://hello.com" ; exit 1 ;;
    esac
done

# do something with the variables -- in this case the lamest possible one :-)
echo "RX = $RX"
echo "TX = $TX"
echo "BAUDRATE = $BAUDRATE"
echo "URL = $URL"
tmpfile=$(mktemp img-XXXXXX.py)
echo $tmpfile
#Exprimée en seconde
attente_min=60
attente_max=300

echo "attente_min = $attente_min"
echo "attente_max = $attente_max"

while true
do
	attente=`shuf -i $attente_min-$attente_max -n 1`
	echo "Prochaine impression dans $attente secondes"
	sleep $attente

	python3 getRandomLink.py $URL randomLink.txt
	LINK=$(head -n 1 randomLink.txt)
	rm randomLink.txt

	#wget "https://webcap.deuxfleurs.fr/capture/$LINK" -O downloadedImage1.jpg && python3 imgtopy.py downloadedImage1.jpg "$tmpfile" && echo ">>>>>>>> $tmpfile" && python3 print.py "$TX" "$RX" "$BAUDRATE" 48 "$tmpfile"
	wget "https://webcap.deuxfleurs.fr/capture/$LINK" -O downloadedImage1.jpg 
	python3 imgtopy.py downloadedImage1.jpg "$tmpfile" 
	python3 print.py "$TX" "$RX" "$BAUDRATE" 48 "$tmpfile"

	rm downloadedImage1.jpg
	rm converteddownloadedImage1.jpg
	rm "$tmpfile"
done
