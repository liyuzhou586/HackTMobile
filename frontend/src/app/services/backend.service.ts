import {Injectable} from '@angular/core'
import {HttpClient, HttpErrorResponse} from '@angular/common/http';
import {Observable, BehaviorSubject} from 'rxjs';
import {map} from 'rxjs/operators';
import {environment} from '../../environments/environment';

@Injectable()
export class BackendService {
  private queryRs = new BehaviorSubject<any>(null);
  public queryRs$ = this.queryRs.asObservable();
  constructor(private http: HttpClient) {
  }

  private static _handleError(err: HttpErrorResponse | any) {
    return Observable.throw(err.message || 'Error: Unable to complete request.');
  }

  updateQueryRs(data) {
    this.queryRs.next(data);
  } 

  // Very important to define a responseType
  deviceRec(): Observable<any> {
    return this.http
      .get(`${environment.apiUrl}/device`,{responseType: 'text'})
  }

  // Very important to define a responseType
  aboutUs(): Observable<any> {
    return this.http
      .get(`${environment.apiUrl}/about`,{responseType: 'text'});
  }

  // Very important to define a responseType, may change to json format so that we can do Javascript layer visualization
  // Format of this query stuff is {"queryParam":"KEVIN"}
  queryStuff(queryJson): Observable<any> {
    return this.http
      .post(`${environment.apiUrl}/queryStuff1`,queryJson,{responseType: 'text'});
  }
}