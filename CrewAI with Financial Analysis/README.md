### EN
### CrewAI Key Takeaways:

CrewAI allows you to create collaborative agents that work together seamlessly. Here’s a breakdown of how it works:

- **Agent Roles & Description**: Each agent has a defined role, a goal, and a backstory (description).
- **Tools for Agents**: You can assign a specific set of tools for each agent, including CrewAI tools, LangChain tools, or custom tools you create.
- **Task Definition**: Each agent is given a task with detailed instructions and expected outcomes. Tasks can also include extra parameters such as tools (which can override the agent’s default tools) and various output formats.
- **Creating the Crew**: You create a "Crew" with a manager, assigning agents and their tasks in the correct order. The process ensures the agents collaborate effectively to execute the tasks and deliver the final answer.
- **Collaboration Process**: The agents work together, following a hierarchical process where the manager decides which agent handles each task, overseeing memory transitions and refining results. Agents may also ask for further improvements.
- **Agent Task Delegation**: Regardless of the process chosen, agents can delegate tasks to each other to optimize results.

### Tools:
For this example, I used two main tools:
- One to collect historical prices.
- Another to gather news articles from Yahoo Finance.

Additionally, I used two CrewAI tools: the **Scrape** tool and the **Search** tool.

### Use Case:

I asked the CrewAI agent to:
- Analyze trends for Apple.
- Extract sentiment analysis from news articles.
- Suggest trading strategies based on the insights.

### Key Insights from Practicing with CrewAI:

- **Intermediate Results Matter**: The intermediary analysis provided by the agents was incredibly insightful, offering more valuable information than the final answer.
- **News Analysis**: The agents highlighted key news insights that influenced their proposed trading strategies, especially regarding recent developments like the integration of Microsoft Copilot AI in PCs.
- **Final Results**: While the final result was accurate, it was rather generic and could apply to any financial instrument.
  ==> I found the process of collaboration much more engaging than the final result.
- **Iteration Control**: I limited the number of iterations to 3, and even with this, the intermediate analyses were quite interesting.
- **Be Specific in Instructions**: When specifying agent tasks, be clear and specific. For example, asking the same agent to analyze both historical data and news articles for different purposes led to the agent focusing on only one task.
- **Be Cautious with LLM Selection**: Specify which LLM you want to use for each agent. If left unspecified, CrewAI defaults to GPT-4, which can be costly, especially with a default iteration count of 25. (I kept an eye on my OpenAI costs during the process.)

### TR
### CrewAI Anahtar Çıkarımlar:

CrewAI, birlikte çalışan ajanlar oluşturmanıza olanak tanır. İşte nasıl çalıştığının bir özeti:

- **Ajan Rolleri ve Tanımı**: Her ajanın belirli bir rolü, amacı ve geçmişi (açıklaması) vardır.
- **Ajanlar için Araçlar**: Her ajana belirli araçlar atayabilirsiniz, bunlar CrewAI araçları, LangChain araçları veya kendi oluşturduğunuz araçlar olabilir.
- **Görev Tanımlaması**: Her ajana, ayrıntılı talimatlar ve beklenen sonuçlar içeren bir görev verilir. Görevler, ayrıca araçlar (ajanın varsayılan araçlarını geçersiz kılabilir) ve çeşitli çıktı formatları gibi ekstra parametreler de içerebilir.
- **Crew Oluşturma**: Bir "Crew" oluşturursunuz ve yöneticiyi belirler, ajanları ve görevlerini doğru sırada atarsınız. Süreç, ajanların etkili bir şekilde işbirliği yaparak görevleri yerine getirmesini ve nihai cevabı sağlamasını garanti eder.
- **İşbirliği Süreci**: Ajanlar işbirliği yaparak, hangi ajanın hangi görevi yapacağına yöneticinin karar verdiği hiyerarşik bir süreci takip ederler. Ayrıca, sonuçları geliştirmek için ajanlar birbirlerinden iyileştirme talep edebilir.
- **Ajan Görev Devri**: Seçilen işbirliği sürecine bakılmaksızın, ajanlar birbirlerine görev devredebilirler.

### Araçlar:
Bu örnekte kullandığım iki ana araç şunlardı:
- Bir araç, tarihsel fiyatları toplamak için kullanıldı.
- Diğer araç, Yahoo Finance’dan haber makaleleri toplamak için kullanıldı.

Ayrıca, iki CrewAI aracı kullandım: **Scrape** aracı ve **Search** aracı.

### Kullanım Durumu:

CrewAI ajanına şunları sordum:
- Apple için trend analizleri sağlayın.
- Haber makalelerinden duygu analizi yapın.
- Bu bulgulara dayalı ticaret stratejileri önerin.

### CrewAI ile Çalışmanın Anahtar Çıkarımları:

- **Ara Sonuçlar Önemli**: Ajanların sağladığı ara analizler, nihai yanıttan çok daha değerli ve içgörülüydü.
- **Haber Analizi**: Ajanlar, ticaret stratejilerini önerirken özellikle Microsoft Copilot AI'nin PC'lerde entegrasyonu gibi güncel gelişmeleri dikkate alarak haberlerdeki önemli analizleri vurguladılar.
- **Nihai Sonuçlar**: Nihai sonuç doğruydu ancak oldukça genel bir çözüm sunuyor ve her türlü finansal araç için uygulanabilir.
  ==> İşbirliği süreci, nihai sonuçtan daha ilgi çekiciydi.
- **İterasyon Kontrolü**: İterasyon sayısını 3 ile sınırladım ve bu sayede ara analizlerde ilginç bulgular elde ettim.
- **Talimatlarda Net Olun**: Ajanlara verdiğiniz görevlerin tanımlarında net ve spesifik olun. Örneğin, aynı ajana hem tarihsel verileri analiz etmeyi hem de haber makalesinden duygu analizi yapmayı söylediğimde, ajanın sadece birine odaklandığını gördüm.
- **Kullanılacak LLM Seçimi**: Hangi LLM'yi kullanacağınızı belirtmeyi unutmayın. Aksi takdirde, CrewAI varsayılan olarak GPT-4'ü seçer ve bu oldukça pahalı olabilir, özellikle varsayılan iterasyon sayısı 25 olduğunda. (Bu süreçte OpenAI maliyetlerini izlemeyi unutmuyordum.)
