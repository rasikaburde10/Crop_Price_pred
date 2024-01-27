def km(self,csv_name):
        K=2
        self.name = csv_name
        dataset = pd.read_csv(csv_name)
        X = dataset[["WPI","Year"]]
        Centroids = (X.sample(n=K))
        #Visualise data points
       # plt.scatter(X["WPI"],X["Year"],c='black')
       # plt.scatter(Centroids["WPI"],Centroids["Year"],c='red')
       # plt.xlabel('WPI')
        #plt.ylabel('Year')
       # plt.show()
        
        diff = 1
        j=0

        while(diff!=0):
            XD=X
            i=1
            for index1,row_c in Centroids.iterrows():
                ED=[]
                for index2,row_d in XD.iterrows():
                    d1=(row_c["WPI"]-row_d["WPI"])**2
                    d2=(row_c["Year"]-row_d["Year"])**2
                    d=np.sqrt(d1+d2)
                    ED.append(d)
                X[i]=ED
                i=i+1

            C=[]
            for index,row in X.iterrows():
                min_dist=row[1]
                pos=1
                for i in range(K):
                    if row[i+1] < min_dist:
                        min_dist = row[i+1]
                        pos=i+1
                C.append(pos)
            X["Cluster"]=C
            Centroids_new = X.groupby(["Cluster"]).mean()[["Year","WPI"]]
            if j == 0:
                diff=1
                j=j+1
            else:
                diff = (Centroids_new['Year'] - Centroids['Year']).sum() + (Centroids_new['WPI'] - Centroids['WPI']).sum()
                print(diff.sum())
            Centroids = X.groupby(["Cluster"]).mean()[["Year","WPI"]]
            print(Centroids)
            
            
            color=['blue','green','cyan']
            for k in range(K):
                data=X[X["Cluster"]==k+1]
                plt.scatter(data["WPI"],data["Year"],c=color[k])
            plt.scatter(Centroids["WPI"],Centroids["Year"],c='red')
            plt.xlabel('WPI')
            plt.ylabel('Year')
            plt.show()
