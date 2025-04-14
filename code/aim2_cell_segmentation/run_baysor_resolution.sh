
#!/bin/bash
module load gcc

for x in {3..9}; do
  for y in {0..9}; do
    (
      INPUT="/home/jiyaoz/statsproject/xenium_mouse_brain/grid_transcript/transcripts_x${x}_y${y}.parquet"
      OUTPUT_DIR="/home/jiyaoz/statsproject/xenium_mouse_brain/baysor_output/x${x}_y${y}"
    
      mkdir -p $OUTPUT_DIR

      /home/jiyaoz/statsproject/baysor/bin/baysor/bin/baysor run $INPUT \
          -o $OUTPUT_DIR \
          -m 30 \
          -s 5 \
          -x x_location -y y_location -z z_location \
          -g feature_name
    )
    sleep 2
  done
done


