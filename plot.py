import matplotlib.pyplot as plt

sequence_lengths = ['128', '256', '512', '1024', '2048', '4096']
ssms = [994.305280006864, 1404.1936799945322, 6261.361887992415, 8791.839040063960, 11350.226864239563, 17298.857776310895]
llm = [2910.842224117492, 4129.160704118529, 20168.88739241741, 29353.87214457207, 40025.97928106363, 71315.86652929096]

ssms_ratio = [s / (s + l) for s, l in zip(ssms, llm)]
llm_ratio = [l / (s + l) for s, l in zip(ssms, llm)]

plt.figure(figsize=(10, 6))

plt.bar(sequence_lengths, ssms_ratio, label='SSMs', color='#dae8fc')
plt.bar(sequence_lengths, llm_ratio, bottom=ssms_ratio, label='LLMs', color='#f8cecc')

plt.xlabel('Sequence Length')
plt.ylabel('Runtime Breakdown Ratio')
plt.title('Runtime Breakdown of SSMs and LLMs when Scaling Sequence Length')
plt.legend()
plt.tight_layout()

plt.show()
