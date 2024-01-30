"use strict";

import { performance } from "perf_hooks";

// Solve using recursion without memoization
function lengthOfLongestCommonSubsequence(
  sequence1,
  sequence2,
  firstSeqLength,
  secondSeqLength
) {
  if (firstSeqLength == 0 || secondSeqLength == 0) {
    return 0;
  }

  if (sequence1[firstSeqLength - 1] == sequence2[secondSeqLength - 1]) {
    return (
      lengthOfLongestCommonSubsequence(
        sequence1.slice(0, -1),
        sequence2.slice(0, -1)
      ) + 1
    );
  }

  return Math.max(
    lengthOfLongestCommonSubsequence(
      sequence1.slice(0, -1),
      sequence2,
      firstSeqLength - 1,
      secondSeqLength
    ),
    lengthOfLongestCommonSubsequence(
      sequence1,
      sequence2.slice(0, -1),
      firstSeqLength,
      secondSeqLength - 1
    )
  );
}
var seq1 = "ABCOSYEWNDKYSSHkJDFISDIPAKD";
var seq2 = "BDCABAJEUDJGSSEKDJAFHIDLLSAPD";
const startTime = performance.now();
var length = lengthOfLongestCommonSubsequence(
  seq1,
  seq2,
  seq1.length,
  seq2.length
);
const endTime = performance.now();

console.log(`Longest common subsequence length is ${length}`);
console.log(
  `Computation time for recursion is ${endTime - startTime} milliseconds`
);

// Solve using dynamic programming with top bottom approach
const memory = {};
function lengthOfLongestCommonSubsequenceDynamicProgramming(
  sequence1,
  sequence2,
  firstSeqLength,
  secondSeqLength
) {
  const key = `${firstSeqLength}-${secondSeqLength}`;
  const memorizedValue = memory[key];

  if (memorizedValue != undefined) {
    return memorizedValue;
  }

  if (firstSeqLength == 0 || secondSeqLength == 0) {
    return 0;
  }
  const updateFirstSeqLength = firstSeqLength - 1;
  const updateSecondSeqLength = secondSeqLength - 1;

  if (sequence1[updateFirstSeqLength] == sequence2[updateSecondSeqLength]) {
    memory[key] =
      lengthOfLongestCommonSubsequenceDynamicProgramming(
        sequence1.slice(0, -1),
        sequence2.slice(0, -1),
        updateFirstSeqLength,
        updateSecondSeqLength
      ) + 1;
    return memory[key];
  }

  const topLongestCommonSubsequence =
    lengthOfLongestCommonSubsequenceDynamicProgramming(
      sequence1.slice(0, -1),
      sequence2,
      updateFirstSeqLength,
      secondSeqLength
    );
  const bottomLongestCommonSubsequence =
    lengthOfLongestCommonSubsequenceDynamicProgramming(
      sequence1,
      sequence2.slice(0, -1),
      firstSeqLength,
      updateSecondSeqLength
    );
  memory[key] = Math.max(
    topLongestCommonSubsequence,
    bottomLongestCommonSubsequence
  );
  return memory[key];
}
var seq1 = "ABCOSYEWNDKYSSHkJDFISDIPAKD";
var seq2 = "BDCABAJEUDJGSSEKDJAFHIDLLSAPD";
const sTime = performance.now();
var length = lengthOfLongestCommonSubsequenceDynamicProgramming(
  seq1,
  seq2,
  seq1.length,
  seq2.length
);
const eTime = performance.now();

console.log(`Longest common subsequence length is ${length}`);
console.log(
  `Computation time for dynamic programming is ${eTime - sTime} milliseconds`
);

// Solving longest common subsequence problem using bottom up
function lengthOfLongestCommonSubsequenceBottomUpApproach(
  seq1,
  seq2,
  len1,
  len2
) {
  const store = new Map();
  let maxLen = 0;

  for (let i = 0; i < len1; i++) {
    for (let j = 0; j < len2; j++) {
      const key = `${i}-${j}`;
      const key1 = i - 1;
      const key2 = j - 1;

      if (seq1[i] == seq2[j]) {
        const storedVal = store.get(`${key1}-${key2}`) || 0;
        store.set(key, storedVal + 1);
      } else {
        const storeVal1 = store.get(`${key1}-${j}`) || 0;
        const storeVal2 = store.get(`${i}-${key2}`) || 0;
        store.set(key, Math.max(storeVal1, storeVal2));
      }
      maxLen = Math.max(maxLen, store.get(key));
    }
  }
  return maxLen;
}
