def smithWaterman(seq1, seq2, match, mismatch, gapA, gapB):
  traceback = [[None] * (len(seq1)+1) for i in range(len(seq2)+1)]
  lines = [[0] * (len(seq1) + 1)]
  for i in range(len(seq2)):
    lines.append([0] + [None] * len(seq1))

  gap_repeat = 1
  for i in range(1, len(seq2)+1):
    for j in range(1, len(seq1)+1):
      status = seq1[j-1] == seq2[i-1]
      if status:
        status = match
      else:
        status = mismatch
      gap_number = gapA + gapB * gap_repeat
      up = lines[i-1][j] + gap_number
      diag = lines[i-1][j-1] + status
      left = lines[i][j-1] + gap_number
      best = max(up, left, diag)
      if best == left or best == up:
        gap_repeat += 1
      else:
        gap_repeat = 1
      lines[i][j] = max(best, 0)
      result = ""
      if best == up:
        result += ".up"
      if best == diag:
        result += ".diag"
      if best == left:
        result += ".left"
      traceback[i][j] = result

  traceback_start = 0
  for line in lines:
    if max(line) > traceback_start:
      traceback_start = max(line)

  alignment = []
  for i in range(len(lines)):
    for j in range(len(lines[i])):
      if lines[i][j] == traceback_start:
        alignment.append((i,j))
        break

  alignment1 = ""
  alignment2 = ""
  score = 0
  for n in range(max(len(seq1), len(seq2))):
    try:
      current_i = alignment[-1][0]
      current_j = alignment[-1][1]
      previous = traceback[current_i][current_j]
      if lines[current_i][current_j] == 0:
        break
      if "diag" in previous:
        alignment1 += seq1[current_j-1]
        alignment2 += seq2[current_i-1]
        alignment.append((current_i-1,current_j-1))
        
      elif "up" in previous:
        alignment1 += "-"
        alignment2 += seq2[current_i-1]
        alignment.append((current_i-1,current_j))
      else:
        alignment1 += seq1[current_j-1]
        alignment2 += "-"
        alignment.append((current_i,current_j-1))
    except:
      pass
  alignment1 = alignment1[::-1]
  alignment2 = alignment2[::-1]
  gap_repeat_score = 1
  gap_number_score = gapA + gap_repeat_score * gapB
  for i in range(len(alignment1)):
    if alignment1[i] == '-' or alignment2[i] == '-':
      score += gap_number_score
      gap_repeat_score += 1
    elif alignment1[i] == alignment2[i] :
      score += match
      gap_repeat_score = 1
    else:
      score += mismatch
      gap_repeat_score = 1
  result = (alignment1, alignment2, score)
  return(result)
